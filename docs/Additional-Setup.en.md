# Additional Setup
Whether you're here after using the [drag-and-drop archive](Drag-and-Drop-Archive.md) or using the [main optimisation](Main-Optimisation.md), we still have to perform some setup for the best experience.

## Optimal Game Settings
???+ note
    These options are optimal for most. If your PC is weaker - feel free to set them lower. If your PC is stronger - feel free to set them higher, but don't blame me for the issues.
??? info "Console Settings"
    These settings were set on console versions on the game and the game is most optimized towards those. They're included for the sake of having a complete list.
=== "1.0.8.0"
    | Setting | Optimal Setting | Console Setting | Description | 
    | :-----: | :-------------: | :-----------: | :---------: |
    | Video Mode | Your native resolution(max option, usually) | 1280x720 on Xbox 360; 1152x640 on PlayStation 3; both ran at 20-30 FPS | This setting controls your monitor resolution, or, if `-windowed` launch option is set - game's window size. |
    | Aspect Ratio | Auto | Auto | This setting controls the aspect ratio relative to your monitor resolution. |
    | Texture Quality | High | Medium | This setting controls the resolution of all textures. |
    | Reflection Resolution | Very High | Medium | This setting controls the resolution of reflections - mainly car reflections (but if you're using [FusionFix](/Essential-Modding/FusionFix.md) or [Shader Fixes](/Essential-Modding/Shader-Fixes.md), it won't affect the resolution) |
    | Water Quality | Medium or Very High | Medium | This setting controls the density and intensity of waves in water, as well as water samples. Medium is reccomended due to being less extreme and more realistic. It does not affect the resolution of water's reflection. |
    | Shadow Quality | High | Medium | This setting controls the resolution, as well as the render distance, of shadows. Medium and Low rely on static shadows much more than High. Very High consumes ~20 FPS |
    | Night Shadows | High or Very High | Off | This setting controls the resolution of dynamic shadows off cars' headlights. [FusionFix](/Essential-Modding/FusionFix.md) allows to enhance it by adding dynamic shadows to most objects. |
    | Texture Filter Quality | Anisotropic 16x | Anisotropic 1x | This setting controls anisotropic filtering. |
    | View Distance | Between 21 and 70 | 21 | This setting controls main LOD render distance for stuff like buildings and vehicles. Setting the option above 70 is known to produce instability and artefacts, as well as negatively impact the framerate |
    | Detail Distance | Between 10 and 70 | 10 | This setting controls secondary LOD render distance for secondary props(such as trashcans). Setting the option above 70 may produce instability and artefacts |
    | Vehicle Density | Preference - preferably below 90 | 33 | This setting controls the density of traffic. Setting the option too high might prove travelling by car too troublesome, especially with unstable traffic AI that can occasionally create random blocks even on straight roads and bridges |
    | Definition | Off | Off | This setting controls Depth of Field and Motion Blur - however, it is also known to have issues with blurred image on PC and effects that simply don't scale up in resolution - use [FusionFix](/Essential-Modding/FusionFix.md) or [Shader Fixes](/Essential-Modding/Shader-Fixes.md) to solve the problem |
    | VSync | Off | On | This setting controls Vertical Synchronisation. We're using the one bundled with DXVK instead for it's much better framepacing, aswell as [FusionFix](/Essential-Modding/FusionFix.md)'s FPS limiter |