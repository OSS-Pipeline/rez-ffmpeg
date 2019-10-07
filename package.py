name = "ffmpeg"

version = "4.2.1"

authors = [
    "Fabrice Bellard",
    "Michael Niedermayer"
]

description = \
    """
    FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles and
    related metadata.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "yasm-1+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "ffmpeg",
    "ffprobe"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "ffmpeg-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.FFMPEG_BINARY_PATH.set("{root}/bin")
    env.FFMPEG_INCLUDE_PATH.set("{root}/include")
    env.FFMPEG_LIBRARY_PATH.set("{root}/lib")
