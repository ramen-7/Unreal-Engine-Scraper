<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/troubleshooting-smpte-2110-in-unreal-engine?application_version=5.7 -->

# Troubleshooting SMPTE 2110

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. [Using SMPTE 2110 with nDisplay](/documentation/en-us/unreal-engine/using-smpte-2110-with-ndisplay "Using SMPTE 2110 with nDisplay")
9. Troubleshooting SMPTE 2110

# Troubleshooting SMPTE 2110

A guide for resolving common problems when using SMPTE 2110 in Unreal Engine.

![Troubleshooting SMPTE 2110](https://dev.epicgames.com/community/api/documentation/image/4b526fd6-c4e7-4c12-9463-1a5cfb0effb9?resizing_type=fill&width=1920&height=335)

 On this page

This guide is for troubleshooting problems you might encounter when using SMPTE 2110 with NVIDIA Rivermax.

* In the log, if you expect your system to support GPUDirect but you see the following message:

  `Cuda device doesn't support RDMA. GPUDirect won't be available for Rivermax`

  Verify your environment variables and make sure `RIVERMAX_ENABLE_CUDA` is set to 1.
* When opening a RivermaxMediaSource, if you get the following warning in the log:

  `Could not attach flow to stream. Status: 13.`

  You are using a ConnectX-6 card (not a BlueField-2), so verify the **Time Source** in Unreal Engine’s project settings and set it to **System**.

  [![The Time Source setting for the Nvidia Rivermax plugin.](https://dev.epicgames.com/community/api/documentation/image/d9fc006d-5c9f-4aa6-8e42-bb7638e30db6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9fc006d-5c9f-4aa6-8e42-bb7638e30db6?resizing_type=fit)

  The Time Source setting for the Nvidia Rivermax plugin.
* When opening a RivermaxMediaSource, if the displayed image is rainbow-colored and this is not expected, make sure these commands show the same output:
  `mlxconfig.exe q | findstr "FLEX_PARSER_PROFILE_ENABLE PROG_PARSE_GRAPH"`

  [![Validate these commands have identical output.](https://dev.epicgames.com/community/api/documentation/image/65a2f86a-54c9-45df-a99a-f1d73229b093?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/65a2f86a-54c9-45df-a99a-f1d73229b093?resizing_type=fit)

  Validate these commands have identical output.
* If you see tearing on the wall when using ST 2110 to drive it, validate PTP on all nodes.

  1. Use Putty to connect to the COM port of your BlueField-2 card and login as root.
  2. In the root folder, run the `firefly_monitor.sh` script. This verifies that the DOCA container is running, and prints out PTP status.

     [![The output of firefly_monitor.sh.](https://dev.epicgames.com/community/api/documentation/image/85693c42-76e7-4e1e-a88d-cacec70cd6ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/85693c42-76e7-4e1e-a88d-cacec70cd6ca?resizing_type=fit)

     The output of firefly\_monitor.sh.
  3. Validate that each node has the same value for `gmIdentity` (grandmaster clock identity), otherwise they won’t have the same time reference.
  4. Verify that the values of `gmPresent` and `ptp_stable` are valid.

## Important Information

* **For UE 5.3-5.4, will be removed in the future:** There is a limiting factor on network packet size and pixel grouping with respect to SMPTE 2110. Due to that limit, some resolutions will require at least one packet to be of a different size than the rest. This is known to cause an inter-packet jitter in Rivermax. We recommend using standard resolutions, as those resolutions do not face this issue. However, if this isn’t possible, UE will still attempt to divide frame data into evenly sized packets; if that doesn’t work, the last packet per frame will be a different size than the rest.
  You can disable the ability to send uneven packets by setting the following cvar: `Rivermax.Output.EnableMultiSRD=0`
  If the resolution isn’t divided into same sized packets, the following message appears in the UE Log:
  "Due to resolution YOUR\_RESOLUTION, row data will be sent over multiple packets with varied sizes."
* For version 1.41.11 of Rivermax and UE 5.4, the default value of the `Rivermax.Output.ForceSkip` console variable has changed to 0, which is the recommended value. In UE 5.3 Rivermax.Output.ForceSkip=1 was used and was known to cause issues after a prolonged playback. This cvar was an artificial way for UE to handle the issues fixed natively by the `RIVERMAX_TX_DELAY_ADAPTIVE_AUTO_CORRECTION_FACTOR` environment variable provided by Rivermax 1.41.11

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [graphics](https://dev.epicgames.com/community/search?query=graphics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Important Information](/documentation/en-us/unreal-engine/troubleshooting-smpte-2110-in-unreal-engine?application_version=5.7#important-information)
