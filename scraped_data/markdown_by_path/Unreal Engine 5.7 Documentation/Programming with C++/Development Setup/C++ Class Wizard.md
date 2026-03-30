<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine?application_version=5.7 -->

# C++ Class Wizard

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
5. [Programming with C++](/documentation/en-us/unreal-engine/programming-with-cplusplus-in-unreal-engine "Programming with C++")
6. [Development Setup](/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine "Development Setup")
7. C++ Class Wizard

# C++ Class Wizard

An overview of the C++ Class Wizard in Unreal Engine.

![C++ Class Wizard](https://dev.epicgames.com/community/api/documentation/image/0ff4a977-038d-4609-abe4-e9d2803b0c98?resizing_type=fill&width=1920&height=335)

Choose your operating system

Windows
macOS
Linux


The **C++ Class Wizard** provides a fast and easy way to add native C++ code classes into your project for you to extend
with your own functionality, if you wish. This converts a content-only project into a code project. You can access the C++ Class Wizard and create a new C++ class by following these steps:

Check [Setting Up Visual Studio](/documentation/404) to ensure that you have a compatible version of Visual Studio installed before proceeding. For information about the correct version of Xcode, refer to the [Unreal Engine Release Notes](/documentation/en-us/unreal-engine/whats-new).

1. In the main editor, select **Tools > New C++ Class...**

   ![Open a new CPP class from the menu bar.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1c62e718-7b3e-4413-9760-5213c323deef/new-cpp-class.png "New CPP Class")
2. The **C++ Class Wizard** will appear and show **Common Classes** by default. If you do not see the class you are looking for, you can view the entire Class hierarchy listing by selecting **All Classes**.

   |  |  |
   | --- | --- |
   | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bb33fb3-7788-44dd-8697-96410c95331a/common-classes.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e462570-eff4-4815-9319-d212ac36e86f/all-classes.png) |
   | Common Classes | All Classes |
3. Choose the Class you want to add. For the purposes of this demonstration, we will choose to create a new **Actor** Class. Select the **Actor** Class, then click **Next >**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d51af22-f6a9-405d-ba71-117e92d7c465/choose-actor-class.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d51af22-f6a9-405d-ba71-117e92d7c465/choose-actor-class.png)
4. You will then be prompted to enter a **Name** for your new Class. Do so, then click **Create Class**. This will create the header (`.h`) and source (`.cpp`) files.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/746eb833-ed95-4337-bc19-52524e0c8f3a/name-new-actor-class.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/746eb833-ed95-4337-bc19-52524e0c8f3a/name-new-actor-class.png)



   Class names can only contain alphanumeric characters and cannot contain spaces. The field will notify you if you enter an invalid name.
5. In Unreal Engine, **Live Coding** is now enabled by default. A Live Coding window will appear and compile the new class files that were created.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c8bc966-829d-4f3c-bcfb-f208aa7e9f10/live-coding.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c8bc966-829d-4f3c-bcfb-f208aa7e9f10/live-coding.png)
6. The code will immediately open in Visual Studio, ready for editing.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d2592c6-86bd-4d12-a1a2-53ccebcb6593/code-in-vs.png)


   The code will immediately open in Xcode, ready for editing.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5a9191d8-09d2-4744-8552-884c7b5c0e4f/codeediting_xcode.png)

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

Related documents

[Coding Standard

![Coding Standard](https://dev.epicgames.com/community/api/documentation/image/3abcd8ff-9c68-4d73-97ab-d698f9fcfb07?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine)

[Compiling Game Projects

![Compiling Game Projects](https://dev.epicgames.com/community/api/documentation/image/b090880f-d297-49ff-ab97-303f704185b6?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/compiling-game-projects-in-unreal-engine-using-cplusplus)
