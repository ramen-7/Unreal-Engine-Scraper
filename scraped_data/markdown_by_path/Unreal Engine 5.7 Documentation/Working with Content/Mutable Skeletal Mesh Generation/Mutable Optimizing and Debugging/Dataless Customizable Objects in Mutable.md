<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dataless-customizable-objects-in-mutable?application_version=5.7 -->

# Dataless Customizable Objects in Mutable

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Mutable Skeletal Mesh Generation](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine "Mutable Skeletal Mesh Generation")
7. [Mutable Optimizing and Debugging](/documentation/en-us/unreal-engine/mutable-optimizing-and-debugging-in-unreal-engine "Mutable Optimizing and Debugging")
8. Dataless Customizable Objects in Mutable

# Dataless Customizable Objects in Mutable

A Dataless Customizable Object uses in-game changeable Parameter nodes.

On this page

A **Dataless Customizable Object** is a normal **Customizable Object** whose input nodes are in-game changeable **Parameter Nodes**.

You can convert any Customizable Object to dataless by replacing the following nodes:

| Constant Nodes | Parameter Nodes |
| --- | --- |
| Texture Node | Texture Parameter Node |
| Skeletal Mesh Node | Skeletal Mesh Parameter Node |
| Material Node | Material Parameter Node |
| Table Node | T / SK / M Node |

It is not a requirement to replace all nodes. You can mix and match Constant and Parameter nodes. In short, you will only take advantage of dataless on those inputs which are Parameter nodes.

### Improvements Over Customizable Objects

* **Faster compilation time**: Inputs from Parameter nodes are not compiled, instead they are converted at runtime.
* **Encryption**: Now encryption works out of the box. Since inputs are no longer compiled (they are normal **UObjects**), they can now be encrypted as usual.
* **Regular UE workflow**: With the old Constant nodes, you had to keep in mind that meshes and parameters would be embedded in the Customizable Object in a special cook process, and the original assets would be editor-only. With the new dataless system, it works just like any other UE system-like materials.
* **Possibly smaller packages**: Previously if an input was referenced outside of Mutable, it was included in the package twice: once as a compiled **Mutable Resource** and once as a UObject, which is why it wasn’t recommended. Since Parameter inputs are no longer compiled, this is no longer the case.

### Limitations

* **Less performant**: Runtime conversions and some optimizations, like generating constants, cannot be applied at compilation time.
* **No available options**: Input parameters do not have a list of available options. This means that gameplay programmers are now responsible for restricting which inputs can be passed in the parameters.

## New Parameters

As regular parameters, the new **Texture**, **Skeletal Mesh** and **Material Parameters** can be set by creating a **Customizable Object Instance** and calling the following functions (Blueprint or C++):

C++

```
|  |  |
| --- | --- |
|  | UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance) |
|  | void SetTextureParameterSelectedOption( |
|  | const FString& TextureParamName, |
|  | UTexture* TextureValue); |
```

UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)
void SetTextureParameterSelectedOption(
const FString& TextureParamName,
UTexture\* TextureValue);

Copy full snippet(4 lines long)

C++

```
|  |  |
| --- | --- |
|  | UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance) |
|  | void SetSkeletalMeshParameterSelectedOption( |
|  | const FString& SkeletalMeshParamName, |
|  | USkeletalMesh* SkeletalMeshValue); |
```

UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)
void SetSkeletalMeshParameterSelectedOption(
const FString& SkeletalMeshParamName,
USkeletalMesh\* SkeletalMeshValue);

Copy full snippet(4 lines long)

C++

```
|  |  |
| --- | --- |
|  | UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance) |
|  | void SetMaterialParameterSelectedOption( |
|  | const FString& MaterialParamName, |
|  | UMaterialInterface* MaterialValue); |
```

UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)
void SetMaterialParameterSelectedOption(
const FString& MaterialParamName,
UMaterialInterface\* MaterialValue);

Copy full snippet(4 lines long)

In addition, in each Parameter node you can specify a **Default Value**. This Default Value is optional and if it is not specified it will be nullptr. You can get these Default Values in the Customizable Object:

C++

```
|  |  |
| --- | --- |
|  | UFUNCTION(BlueprintCallable, Category = CustomizableObject) |
|  | UTexture* GetTextureParameterDefaultValue( |
|  | const FString& InParameterName) const; |
```

UFUNCTION(BlueprintCallable, Category = CustomizableObject)
UTexture\* GetTextureParameterDefaultValue(
const FString& InParameterName) const;

Copy full snippet(3 lines long)

C++

```
|  |  |
| --- | --- |
|  | UFUNCTION(BlueprintCallable, Category = CustomizableObject) |
|  | USkeletalMesh* GetSkeletalMeshParameterDefaultValue( |
|  | const FString& ParameterName) const; |
```

UFUNCTION(BlueprintCallable, Category = CustomizableObject)
USkeletalMesh\* GetSkeletalMeshParameterDefaultValue(
const FString& ParameterName) const;

Copy full snippet(3 lines long)

C++

```
|  |  |
| --- | --- |
|  | UFUNCTION(BlueprintCallable, Category = CustomizableObject) |
|  | UMaterialInterface* GetMaterialParameterDefaultValue( |
|  | const FString& ParameterName) const; |
```

UFUNCTION(BlueprintCallable, Category = CustomizableObject)
UMaterialInterface\* GetMaterialParameterDefaultValue(
const FString& ParameterName) const;

Copy full snippet(3 lines long)

Keep in mind that if a Default Value is set, the referenced objects will be cooked. Also the lifecycle of these objects is the same as the Customizable Object since they are strong references.

Once all parameters have been set. To see the results, you need to call:

C++

```
|  |  |
| --- | --- |
|  | UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance) |
|  | void UpdateSkeletalMeshAsync( |
|  | bool bIgnoreCloseDist = false, |
|  | bool bForceHighPriority = false); |
```

UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)
void UpdateSkeletalMeshAsync(
bool bIgnoreCloseDist = false,
bool bForceHighPriority = false);

Copy full snippet(4 lines long)

## Example

**Regular Nodes**: 
Skeletal Mesh references are shown in the **Reference Viewer** due to having an Editor-Only reference.

[![Normal-constant-parameter-menu](https://dev.epicgames.com/community/api/documentation/image/1a7afecc-45e3-447b-91cd-780aa86c532b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a7afecc-45e3-447b-91cd-780aa86c532b?resizing_type=fit)

In a packaged game, they are not included as UObjects but as Mutable Resources:

[![Skeletal-mesh-as-mutable-resources-in-Blueprints.](https://dev.epicgames.com/community/api/documentation/image/29012148-f677-4a53-85a7-f41ec9823dd6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29012148-f677-4a53-85a7-f41ec9823dd6?resizing_type=fit)

**Dataless Nodes**: 
Notice that only the Skeletal Mesh nodes have been converted to dataless.

[![Dataless-parameter-menu.](https://dev.epicgames.com/community/api/documentation/image/a00bf35f-63c7-422c-9b4b-a50ad31f48ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a00bf35f-63c7-422c-9b4b-a50ad31f48ee?resizing_type=fit)

The Material is still a constant (not a parameter):

[![The-material-is-still-a-constant.](https://dev.epicgames.com/community/api/documentation/image/9b86684e-28c2-4492-b7bf-e4b6a6950169?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b86684e-28c2-4492-b7bf-e4b6a6950169?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Improvements Over Customizable Objects](/documentation/en-us/unreal-engine/dataless-customizable-objects-in-mutable?application_version=5.7#improvementsovercustomizableobjects)
* [Limitations](/documentation/en-us/unreal-engine/dataless-customizable-objects-in-mutable?application_version=5.7#limitations)
* [New Parameters](/documentation/en-us/unreal-engine/dataless-customizable-objects-in-mutable?application_version=5.7#newparameters)
* [Example](/documentation/en-us/unreal-engine/dataless-customizable-objects-in-mutable?application_version=5.7#example)
