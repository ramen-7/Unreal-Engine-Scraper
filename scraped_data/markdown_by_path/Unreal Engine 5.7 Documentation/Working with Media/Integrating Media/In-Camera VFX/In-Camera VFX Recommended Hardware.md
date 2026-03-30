<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-hardware-for-in-camera-vfx-in-unreal-engine?application_version=5.7 -->

# In-Camera VFX Recommended Hardware

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
7. [In-Camera VFX](/documentation/en-us/unreal-engine/in-camera-vfx-in-unreal-engine "In-Camera VFX")
8. In-Camera VFX Recommended Hardware

# In-Camera VFX Recommended Hardware

Details on the hardware recommendations for an in-camera VFX setup with Unreal Engine

![In-Camera VFX Recommended Hardware](https://dev.epicgames.com/community/api/documentation/image/13a018e3-ca8c-45fc-afbd-8f40c9b720bc?resizing_type=fill&width=1920&height=335)

 On this page

An in-camera VFX setup using Unreal Engine requires multiple machines to communicate with each other and drive the LED volume display. This page covers the hardware to consider for your in-camera VFX setup.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a341c729-4cfa-402a-9ebc-73e5164d4a90/image_0.jpg)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a341c729-4cfa-402a-9ebc-73e5164d4a90/image_0.jpg)

An example hardware layout with three render nodes. Click image for full size.

Most LED processors have the option to receive sync either from an external genlock source or from the incoming video signal from the graphics cards. Check what options are available with the LED processors you're using. In the hardware diagram, an external genlock source is providing the sync for the LED processors.

### Recommended Machine Hardware

|  |  |
| --- | --- |
| Workstation | When you select a workstation, it is important that you have adequate space and power for your memory, storage, and graphics hardware. Make sure your workstation has enough space and can support [NVLink](https://www.nvidia.com/en-us/design-visualization/nvlink-bridges/) if you want to utilize multi-GPU, available starting in Unreal Engine 4.26. |
| CPU | In general, you should favor faster clock speeds over more cores. Beyond eight cores, the benefits of additional cores will be more noticeable in the compile time for code and shaders than other use cases. It is recommended that you have at least a three gigahertz (Ghz) clock speed as a starting point. Common examples of CPUs used for the in-camera VFX scenario include the [Intel Xeon](https://www.intel.com/content/www/us/en/products/processors/xeon.html) and [Intel Core i9 processors](https://www.intel.com/content/www/us/en/products/processors/core/i9-processors.html), as well as the [AMD Ryzen 9 3950X](https://www.amd.com/en/products/cpu/amd-ryzen-9-3950x), [AMD Threadrippers](https://www.amd.com/en/products/ryzen-threadripper), and [AMD Threadripper Pro](https://www.amd.com/en/processors/ryzen-threadripper-pro). |
| RAM | 64GB of DDR-4 memory is the recommended minimum for most in-camera VFX scenarios. Additional RAM may be required if your production uses large files. |
| GPU | **Artist workstations**: For artists using [ray tracing](/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) and other advanced rendering features in Unreal Engine, we recommend the professional-level NVIDIA RTX cards:   * [NVIDIA RTX A6000](https://www.nvidia.com/en-us/design-visualization/rtx-a6000) * [NVIDIA RTX A5000](https://www.nvidia.com/en-us/design-visualization/rtx-a5000) * [NVIDIA Quadro RTX 8000](https://www.nvidia.com/en-us/design-visualization/quadro/rtx-8000) * [NVIDIA Quadro RTX 6000](https://www.nvidia.com/en-us/design-visualization/quadro/rtx-6000)   Artists with lighter rendering needs may be able to use the consumer-level NVIDIA RTX cards:   * [NVIDIA GeForce RTX 3080Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080-3080ti/) * [NVIDIA GeForce RTX 3090](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/)   **Render nodes**: [NVIDIA Quadro Sync](https://www.nvidia.com/en-us/design-visualization/solutions/quadro-sync/) is required to synchronize displays across an LED volume. Each render node machine must have this card in addition to its graphics card. You can find more details in NVIDIA's [Quadro Sync II User Guide](https://images.nvidia.com/content/quadro/product-literature/user-guides/Quadro-Sync-II-User-Guide.pdf).  For render nodes with either single or dual GPU, we recommend the following NVIDIA RTX cards:   * [NVIDIA RTX A6000](https://www.nvidia.com/en-us/design-visualization/rtx-a6000) * [NVIDIA Quadro RTX 8000](https://www.nvidia.com/en-us/design-visualization/quadro/rtx-8000) * [NVIDIA Quadro RTX 6000](https://www.nvidia.com/en-us/design-visualization/quadro/rtx-6000)   For a complete list of compatible graphics cards with NVIDIA Quadro Sync, refer to the NVIDIA page for [Quadro Sync](https://www.nvidia.com/en-us/design-visualization/solutions/quadro-sync/).  If you plan to make use of nDisplay's support for rendering to multiple GPUs on a single computer, all graphics cards must also support [NVLINK](https://www.nvidia.com/en-gb/design-visualization/nvlink-bridges/).  We generally recommend using the latest drivers from NVIDIA. In particular, when using multiple GPUs on a single workstation, make sure to use **version R512.59 or later**.  You can find the recommended driver for Virtual Production on [NVIDIA"s Download Drivers page](https://www.nvidia.com/Download/index.aspx). Select your card type and OS and set **Download Type** to **Production Branch / Studio** to find the recommended driver. |
| Video Card | If you plan to use live green-screen compositing, you will need a SDI video card to handle camera input, compositing output, and timecode synchronization. SDI video cards such as the [AJA Kona 5](https://www.aja.com/products/kona-5) and the [Blackmagic DeckLink](https://www.blackmagicdesign.com/products/decklink/techspecs/W-DLK-25) are recommended for live compositing. |
| Storage | Because your project data is localized to each computer, fast local storage is necessary for optimal performance. It is recommended that you use [M.2 Solid State Drives](https://en.wikipedia.org/wiki/M.2) (SSDs), such as the [Samsung 970 Pro](https://www.samsung.com/semiconductor/minisite/ssd/product/consumer/970pro/), as the secondary data drives from the machine's boot drive. |
| Storage Network Card | A 10-Gigabit Ethernet (GbE) Network Interface Controller (NIC) is recommended to maintain high-speed data transfer between operator systems and render machines. |

### Additional Recommended Hardware

|  |  |
| --- | --- |
| Network Switch | Most 10 GbE Layer 2 or Layer 3 type network switches, such as the [Netgear Smart Switch](https://www.netgear.com/business/products/switches/smart/XS716T.aspx#tab-techspecs), should be sufficient for this scenario. |
| Sync Generators | There are wired and wireless options available for sync generators, and it is common to use both for an in-camera VFX set. For example, you can use a wired box to send signals to a wireless one. In the hardware diagram above, the orange line represents the wireless connection from a sync generator to the camera. The following is a list of recommended sync generators:  Wired options:   * [Blackmagic Design Mini Converter Sync Generator](https://www.blackmagicdesign.com/products/miniconverters/techspecs/W-CONM-15) * [AJA GEN10 HD/SD/AES Sync Generator](https://www.aja.com/products/gen10) * [ESE HD-488E/SD HD/SD-SDI Timecode Reader/Generator/Inserter](https://www.bhphotovideo.com/c/product/1201898-REG/ese_hd_488e_sd_hd_sd_sdi_time.html) * [Evertz 5601MSC Master Sync and Clock Generator](https://evertz.com/products/5601MSC) * [Courtyard CY460 Master Synce Generator](http://www.courtyard.co.uk/cy460-master-spg-test-pattern-time-reference-generator/)   Wireless options:   * [Ambient Master Lockit for Master Sync](https://ambient.de/en/product/master-lockit/) * [Ambient Lockit for Remote Sync](https://ambient.de/en/product/lockit/) |
| Display Adapters | * See the NVIDIA [list of standard display adapters](https://nvidia.custhelp.com/app/answers/detail/a_id/4449/~/nvidia-recommended-display-adapters) recommended for the NVIDIA GeForce and Quadro cards. * See [Club-3D CAC 1080](https://www.club-3d.com/detail/2442/displayportt_1.4_to_hdmit_2.0b_hdr_active_adapter) for connecting Display Port 1.4 to HDMI 2.0 on LED processors. * See the [Lightware MX2 Series](https://lightware.com/products/matrices-switchers) for connecting Display Port 1.2 to HDMI 2.0 on LED processors. * Use fiber extenders for longer, uncompressed HDMI connections, such as connecting graphics cards to display ports. The [Lightware fiber extender](https://lightware.com/hdmi20-opt) is recommended for uncompressed HDMI 2.0 4K signals. |
| Video Distribution Amplifier (VDA) | For an in-camera VFX setup, VDAs are typically used to distribute the genlock signal into multiple channels to the render nodes, camera tracking system, the live compositing machine, and sometimes the camera itself. In the diagram above, you can see the lines from the genlock sync are distributed through the distribution amplifier to various other devices in the setup.  The following is a list of recommended VDAs:   * [Shinybow Composite DAs](https://www.shinybowusa.com/shop/index.php?cPath=37_45) * [Kramer](https://www.kramerav.com/us/products/distribution_amplifiers/sdi-distribution-amplifiers) * [VAC](https://vac-brick.com/product-category/video-distribution-amplifier/) |

* [in-camera vfx](https://dev.epicgames.com/community/search?query=in-camera%20vfx)
* [synchronization](https://dev.epicgames.com/community/search?query=synchronization)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Recommended Machine Hardware](/documentation/en-us/unreal-engine/recommended-hardware-for-in-camera-vfx-in-unreal-engine?application_version=5.7#recommendedmachinehardware)
* [Additional Recommended Hardware](/documentation/en-us/unreal-engine/recommended-hardware-for-in-camera-vfx-in-unreal-engine?application_version=5.7#additionalrecommendedhardware)
