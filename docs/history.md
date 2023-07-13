# History
Kreato Linux was started in 2022, mainly because i was fed up with other Linux distributions.

It had a POSIX sh base (nyaa, the package manager was written in POSIX sh) with a bit of C at the start (nyaa-src was built in C, which was for building the rootfs). I killed out nyaa-src pretty quick because of it not utilizing the package manager nyaa, which was a big issue. The another reason was the code being a mess, and was full of shell commands anyway. It was good for a first try atleast, it gave me something that was working.

I replaced nyaa-src with nyaastrap, which was written in POSIX sh just like the package manager and was actually utilizing it. It was pretty buggy and never worked right but atleast was better than nyaa-src.

This was also the time when i packaged the entirety of sway (and its dependencies) and booted it up in real hardware. Was the quite sight to see a year of work finally showing progress. But change was swift after that.

I was fed up with the issues of nyaa (now called nyaa2) like unreadable code in a lot of areas, slow performance, minimalism not being possible in the project without a massive refactor and not great error handling. Nyaastrap being not great wasnt helping either.

That was the time when i replaced nyaa with a rewrite in Nim, a programming language i was quite familiar with since i worked with it for a while. I made a test suite and rewrote nyaastrap too. 
And thats what we are at now. It's going well so far. I hope it continues this way.
