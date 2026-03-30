<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/updating-unreal-engine-on-linux-to-sdl3?application_version=5.7 -->

# Updating Unreal Engine on Linux to SDL3

1. ![Epic Games](https://edc-cdn.net/assets/images/logo-epic.svg)[Developer](/)
2. [Documentation](/documentation/ "Documentation")
3. Unreal Engine
   * [Unreal Engine](/documentation/en-us/unreal-engine)
   * [Fortnite](/documentation/en-us/fortnite)
   * [Twinmotion](/documentation/en-us/twinmotion)
   * [MetaHuman](/documentation/en-us/metahuman)
   * [RealityScan](/documentation/en-us/realityscan)
   * [RealityScan Mobile](/documentation/en-us/realityscan-mobile)
   * [Fab](/documentation/en-us/fab)
4. [Unreal Engine 5.7 Documentation](/documentation/en-us/unreal-engine/unreal-engine-5-7-documentation "Unreal Engine 5.7 Documentation")
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [Linux Game Development](/documentation/en-us/unreal-engine/linux-game-development-in-unreal-engine "Linux Game Development")
7. Updating Unreal Engine on Linux to SDL3

# Updating Unreal Engine on Linux to SDL3

Information on required updates for Unreal Engine on Linux.

On this page

We’ve updated Unreal Engine 5.7 for Linux to use SDL3 build 3.2.10.  This document gives more information on this change and what to expect.

## Compiling and Required Code Changes

You need to change any use of the SDL2 module to SDL3 in your build.cs files.

The main header file for SDL has also changed:

`#include “SDL.h”`   
or  
`#include <SDL.h>`

Needs to be changed to:

`#include “SDL3/SDL.h”`   
or  
`#include <SDL3/SDL.h>`

All SDL header files are under the SDL3 subdir now.  Including the SDL3 module adds the correct include paths to your code.

SDL3 includes a number of API changes.  The best guide for what has changed and how to update code is this web page:

[Migrating to SDL 3.0](https://wiki.libsdl.org/SDL3/README-migration)

One of the bigger changes is the return values from SDL functions.  Functions no longer return negative values, they return success/failure booleans.  Be sure to read the notes in the migration guide.

## Building SDL3

The binaries for SDL3 for both x86-64 and Arm64 are checked into Unreal Engine

`/Engine/Source/ThirdParty/SDL3/SDL-gui-backend/lib/Unix/aarch64-unknown-linux-gnueabi`

`/Engine/Source/ThirdParty/SDL3/SDL-gui-backend/lib/Unix/x86_64-unknown-linux-gnu`

If you need to rebuild these libraries you need to use the Epic scripts in`/Engine/Source/ThirdParty/SDL3/docker`

If you run `/Engine/Source/ThirdParty/SDL3/docker/RunMe.sh` it creates a docker container and builds the SDL library from the `/Engine/Source/ThirdParty/SDL3/SDL-gui-backend` with the correct options for both processor variants and copies the results into the correct directories.This is the only supported way to rebuild the library for use with Unreal Engine.

In the docker directory there is also a script `/Engine/Source/ThirdParty/SDL3/docker/local_build.sh` that builds the x86-64 version of the library using the Linux environment you are in.  This means you have to have installed all the various libraries and tools to build SDL3.  The local build script **is not** suitable for building a library for redistribution but it is a much faster way to quickly rebuild the SDL3 libraries for development testing.  **Never** submit a binary build of the SDL3 libraries built with it, it is **only** for development purposes.

## New and Changed Functionality

With SDL3, we hooked the SDL logging to Unreal Engine’s logging.  This makes any SDL log events visible (under the LogSDL3 category).  When running a debug build of Unreal Engine we set the SDL3 logging level to verbose by default.  SDL3 is not log intensive so even on verbose the output is minimal.  You can control the SDL3 logging using environment variables.

SDL3 handles device DPI and scaling differently than SDL2.  As a result you might find that Unreal Editor as well as apps using Slate will appear with 100% scaling where with SDL2 they would often be scaled based on your screen dimensions.  With SDL3 the application scaling is set using X Windows options.  The easiest way is most likely the settings panel in Ubuntu:

[![Ubuntu settings panel for display scaling](https://dev.epicgames.com/community/api/documentation/image/f1f8df7b-f62f-4665-a0b5-40f2e104a768?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1f8df7b-f62f-4665-a0b5-40f2e104a768?resizing_type=fit)

Unreal Editor follows what you configure there.

SDL3 looks for the video scaling a few different ways:

* First, it checks for the SDL Hint `SDL_HINT_VIDEO_X11_SCALING_FACTOR`.
* If that doesn’t exist, it falls back to `Xft.dpi` which matches other application frameworks like Qt and Gtk.
* If that also doesn’t exist, it tries the XSETTINGS key `Gdk/WindowScalingFactor`.
* If none of those are set/available it then tries the `GDK_SCALE` Environment variable.

Depending on which version of Linux and your X11 Window manager you might need to use different ways to configure the scale that Unreal Editor and UE applications use.

With SDL3, we added support for toggling the `norelativemousemode` using an Environment variable.  When running UE-based applications over services like NiceDCV and Teradici, UE requires you start the application with the command line flag `-norelativemousemode`. With SDL3 you can also set this option by using the environment variable `UE_NORELATIVEMOUSEMODE` which you can set in your`.bashrc` file, for example:

Shell

```
export UE_NORELATIVEMOUSEMODE=1
```

export UE\_NORELATIVEMOUSEMODE=1

Copy full snippet(1 line long)

Users not using a remote desktop application shouldn’t need this, but if you needed `-norelativemousemode` before, the environment variable support makes it much easier to set.

## Known Issues

We entirely removed from this update many of the input and focus workarounds we added to SDL2.  It’s possible that some of those issues or new variants of them still remain.

We removed the SDL2 work-around for unintentional double-clicks when CTL-clicking adjacent selected assets.  CTL-clicking too fast in the Linux File Browser is now seen as a double click.

While Wayland support is compiled into the SDL3 library, Unreal Editor using pure Wayland is unusable.  Mouse click events are not correctly received (though touch events are) and in general there are a number of issues.  X11Wayland support is fine and Editor works as normal in that mode, but if you set `SDL_VIDEODRIVER=wayland` and run using a Wayland window manager, Unreal Editor is not functional.  Support for game targets using Wayland mode is also still untested.

You might notice a quick window border flash when dropping down menus inside Unreal Editor.  This is actually present using SDL2 as well, but with SDL3 the window outline (at least on Ubuntu with the default Window Manager) is much more noticeable.

Using SDL2, it’s a light outline

[![SDL2 window border](https://dev.epicgames.com/community/api/documentation/image/cb0df17e-3789-47bf-b1f9-adccda803ccc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb0df17e-3789-47bf-b1f9-adccda803ccc?resizing_type=fit)

Using SDL3, it’s more of a shadow outline

[![SDL3 window border](https://dev.epicgames.com/community/api/documentation/image/6b392cd3-bbf7-4640-b855-c8357c5230e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6b392cd3-bbf7-4640-b855-c8357c5230e8?resizing_type=fit)

* [linux](https://dev.epicgames.com/community/search?query=linux)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Compiling and Required Code Changes](/documentation/en-us/unreal-engine/updating-unreal-engine-on-linux-to-sdl3?application_version=5.7#compilingandrequiredcodechanges)
* [Building SDL3](/documentation/en-us/unreal-engine/updating-unreal-engine-on-linux-to-sdl3?application_version=5.7#buildingsdl3)
* [New and Changed Functionality](/documentation/en-us/unreal-engine/updating-unreal-engine-on-linux-to-sdl3?application_version=5.7#newandchangedfunctionality)
* [Known Issues](/documentation/en-us/unreal-engine/updating-unreal-engine-on-linux-to-sdl3?application_version=5.7#knownissues)
