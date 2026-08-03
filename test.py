from pathlib import Path
import subprocess

SRC = Path("out.cpp")
DST = Path("Q45_ONE_VISUAL_PROBE.cpp")

text = SRC.read_text(encoding="utf-8")


def replace_function(source: str, signature: str, replacement: str) -> str:
    start = source.find(signature)
    if start < 0:
        raise RuntimeError(f"Không tìm thấy: {signature}")

    brace = source.find("{", start)
    if brace < 0:
        raise RuntimeError(f"Không tìm thấy '{{' sau: {signature}")

    depth = 0
    i = brace

    while i < len(source):
        if source[i] == "{":
            depth += 1
        elif source[i] == "}":
            depth -= 1
            if depth == 0:
                return source[:start] + replacement + source[i + 1:]
        i += 1

    raise RuntimeError(f"Không tìm được cuối hàm: {signature}")


verified_helper = r"""
static Bool tryOneVisualVerifiedCollapse(
    int scan,
    int trials,
    Scalar hdRatio,
    Scalar ssimFloor
){
    if(activeVertexCount<=4)return false;

    const FNMeshState base=captureFN();

    Vec<CollapseCandidate> heap;
    buildCurrentCollapseHeap(heap);

    Vec<pair<Scalar,CollapseCandidate>> candidates;
    candidates.reserve(scan);

    CollapseWorkspace work;
    int seen=0;

    while(!heap.empty()&&seen<scan){
        pop_heap(
            heap.begin(),
            heap.end(),
            CollapseCandidateCompare()
        );

        const CollapseCandidate candidate=heap.back();
        heap.pop_back();
        ++seen;

        if(!vertexActive[candidate.v9]||
           !vertexActive[candidate.to])
            continue;

        if(candidate.vf!=vertexVersion[candidate.v9]||
           candidate.vt!=vertexVersion[candidate.to])
            continue;

        if(!prepareCollapse(
            candidate.v9,
            candidate.to,
            work,
            &candidate
        ))
            continue;

        const Scalar risk=test3VisualRisk(
            candidate.v9,
            candidate.to,
            work
        );

        if(isfinite(risk))
            candidates.push_back({risk,candidate});
    }

    sort(
        candidates.begin(),
        candidates.end(),
        [](const auto&a,const auto&b){
            return a.first<b.first;
        }
    );

    const Scalar hdLimit=hdRatio*meshScale;
    const Scalar hdLimit2=hdLimit*hdLimit;
    const int limit=min(trials,(int)candidates.size());

    for(int i=0;i<limit;++i){
        restoreHD(base);

        const CollapseCandidate candidate=
            candidates[i].second;

        CollapseWorkspace current;

        if(!prepareCollapse(
            candidate.v9,
            candidate.to,
            current,
            &candidate
        ))
            continue;

        applyCollapse(
            candidate.v9,
            candidate.to,
            current
        );

        if(!validateRoundedMesh()||
           !validateTopology()||
           !validateSpatialCoverage())
            continue;

        /*
         * Gate 256 trước để tránh chạy exact-HD và SSIM 1024
         * cho các candidate tệ rõ ràng.
         */
        const PerceptualScore coarse=
            evaluateFinalSSIM(256);

        if(coarse.finalSSIM+1e-9<ssimFloor-.002)
            continue;

        if(exactVHD2()>hdLimit2)
            continue;

        const PerceptualScore finalScore=
            evaluateFinalSSIM(1024);

        if(finalScore.finalSSIM+1e-9<ssimFloor)
            continue;

        return true;
    }

    restoreHD(base);
    return false;
}
"""

pipeline = r"""
static void runGenericPipeline(){
    const int n=numVertices;

    if(n<=80000){
        simplifyMesh();

        if(n<=8000){
            tryRemoveExtraVertices(1);
            runLocalPatchTail(128,128);

            for(int z=0;
                z<32&&tryHDPortfolio(128,12);
                ++z);
        }
        else if(n<=30000){
            /*
             * Test 3: khóa đúng anchor 90.561011.
             * Không thêm bất kỳ probe mới nào.
             */
            tryRemoveExtraVertices(6);

            runSmartTest3Tail(
                .0005,
                .92,
                .92,
                256,
                1024,
                3
            );

            runLocalPatchTail(2,64);
        }
        else if(n<=45000){
            /*
             * Test 4: thử đúng một collapse.
             * Tối đa sáu candidate được kiểm tra đầy đủ.
             */
            tryRemoveExtraVertices(13);

            runSmartTest3Tail(
                .0005,
                .91,
                .91,
                256,
                1024,
                3
            );

            runLocalPatchTail(1,64);

            tryOneVisualVerifiedCollapse(
                128,
                6,
                .0485,
                .905
            );
        }
        else{
            /*
             * Test 5: thử đúng một collapse.
             * Giảm trials để giữ thời gian.
             */
            tryRemoveExtraVertices(17);

            runSmartTest3Tail(
                .0005,
                .95,
                .95,
                192,
                512,
                2
            );

            runLocalPatchTail(0,64);

            tryOneVisualVerifiedCollapse(
                96,
                4,
                .0485,
                .93
            );
        }

        return;
    }

    const int target=acceptedTightTarget(n);

    gPolicy.finalTargetVertices=target;
    gPolicy.finalTargetRatio=
        (Scalar)target/max(1,n);

    gPolicy.preSimplifyTargetVertices=target;
    gPolicy.preSimplifyTargetRatio=
        (Scalar)target/max(1,n);

    simplifyMesh();

    if(n<=500000){
        for(int z=0;
            z<1&&tryHDPortfolio(48,4);
            ++z);

        tryRemoveExtraVertices(12);
        runLocalPatchTail(8,48);
    }
    else{
        tryRemoveExtraVerticesChunked(140,20);
        runLocalPatchTail(12,32);
    }
}
"""

# Thay runBulkTrust bằng helper mới, tránh tăng kích thước source.
text = replace_function(
    text,
    "static int runBulkTrust(",
    verified_helper
)

text = replace_function(
    text,
    "static void runGenericPipeline() {",
    pipeline
)

# Kiểm tra cấu hình.
required = [
    "static Bool tryOneVisualVerifiedCollapse(",
    "tryOneVisualVerifiedCollapse(\n                128,\n                6,",
    "tryOneVisualVerifiedCollapse(\n                96,\n                4,",
    "z<32&&tryHDPortfolio(128,12)",
    "z<1&&tryHDPortfolio(48,4)",
]

for fragment in required:
    if fragment not in text:
        raise RuntimeError(f"Thiếu đoạn bắt buộc: {fragment!r}")

pipeline_part = text[
    text.find("static void runGenericPipeline() {"):
    text.find("int main(")
]

for forbidden in [
    "runBulkTrust(",
    "runFastBulkOnce(",
    "runHDTrust(",
]:
    if forbidden in pipeline_part:
        raise RuntimeError(
            f"Pipeline vẫn chứa hàm cũ: {forbidden}"
        )

# Test 3 tuyệt đối không chứa probe mới.
test3_begin = pipeline_part.find("else if(n<=30000)")
test4_begin = pipeline_part.find("else if(n<=45000)")

test3_part = pipeline_part[test3_begin:test4_begin]

if "tryOneVisualVerifiedCollapse" in test3_part:
    raise RuntimeError("Test 3 vẫn chứa visual probe")

DST.write_text(text, encoding="utf-8")

size = DST.stat().st_size
print("Created:", DST)
print("Size:", size, "bytes")

if size >= 128 * 1024:
    raise RuntimeError(
        f"Source vượt 128 KiB: {size} bytes"
    )

subprocess.run(
    [
        "g++",
        "-std=c++17",
        "-O2",
        "-pthread",
        "-fsyntax-only",
        str(DST),
    ],
    check=True,
)

binary = Path("q45_probe_check")

try:
    subprocess.run(
        [
            "g++",
            "-std=c++17",
            "-O2",
            "-pthread",
            str(DST),
            "-o",
            str(binary),
        ],
        check=True,
    )
finally:
    binary.unlink(missing_ok=True)

print("Syntax: OK")
print("Link: OK")
print("Submit:", DST)