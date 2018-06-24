Title: Embed .srt subtitle into .mkv with ffmpeg
Slug: embed-srt-subtitle-into-mkv-with-ffmpeg
Date: 2018-06-24 21:35:23
Authors: m157q
Category: Note
Tags: CLI
Summary: Note for how to embed .srt subtitle into .mkv video file.


## TL;DR

```bash
ffmpeg -i ${MKV_FILE_PATH} -vf "subtitles='${SRT_FILE_PATH}'" ${OUTPUT_FILE_PATH}
```

## CAUTION

Your `ffmpeg` need `--enable-libass` configuration.
Use `ffmpeg` to check the output, it should be like:

```
ffmpeg version 4.0.1 Copyright (c) 2000-2018 the FFmpeg developers
  built with Apple LLVM version 9.1.0 (clang-902.0.39.1)
  configuration: --prefix=/usr/local/Cellar/ffmpeg/4.0.1 --enable-shared --enable-pthreads --enable-version3 --enable-hardcoded-tables --enable-avresample --cc=clang --host-cflags= --host-ldflags= --enable-gpl --enable-libass --enable-libmp3lame --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libxvid --enable-opencl --enable-videotoolbox --enable-openssl --disable-lzma
--enable-nonfree
  libavutil      56. 14.100 / 56. 14.100
  libavcodec     58. 18.100 / 58. 18.100
  libavformat    58. 12.100 / 58. 12.100
  libavdevice    58.  3.100 / 58.  3.100
  libavfilter     7. 16.100 /  7. 16.100
  libavresample   4.  0.  0 /  4.  0.  0
  libswscale      5.  1.100 /  5.  1.100
  libswresample   3.  1.100 /  3.  1.100
  libpostproc    55.  1.100 / 55.  1.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
```

If you see `--enable-libass` in the output, you don't have to do anything.

Otherwise, you have to reinstall your `ffmpeg` with `--enable-libass`

If you are using macOS with `homebrew`, you can do it by the command below:

```bash
brew install ffmpeg --with-libass
```

---

## Preface

I have one .mkv and one .srt file, and I want to play it on my Chromecast with subtitles.

Unfortunately, Chromecast doesn't support adding subtitle track while playing.

So, I came up with embedding subtitles into video files with `ffmpeg`.

---

## Note

`ffmpeg -i ${MKV_FILE_PATH} -vf "subtitles='${SRT_FILE_PATH}'" ${OUTPUT_FILE_PATH}`

(With `--enable-libass` ffmpeg)

If the font size of the embedded subtitles is too small. You can also change the font size with `force_style` option (even change the font and the color):

```bash
ffmpeg -i ${MKV_FILE_PATH} -vf \
"subtitles='${SRT_FILE_PATH}':force_style='FontName=${FONT_NAME},FontSize=24,PrimaryColour=&HAA00FF00'" \
${OUTPUT_FILE_PATH}
```

---

## References

+ [Install FFMPEG on OS X with HomeBrew to convert Mp4 to WebM](https://gist.github.com/clayton/6196167)
+ [[FFmpeg] 烙印字幕至影像上 (Hardsub)](https://www.mobile01.com/topicdetail.php?f=510&t=4462836)
