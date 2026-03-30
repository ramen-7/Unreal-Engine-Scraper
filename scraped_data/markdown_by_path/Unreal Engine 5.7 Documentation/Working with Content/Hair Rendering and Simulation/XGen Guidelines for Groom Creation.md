<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7 -->

# XGen Guidelines for Groom Creation

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
6. [Hair Rendering and Simulation](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine "Hair Rendering and Simulation")
7. XGen Guidelines for Groom Creation

# XGen Guidelines for Groom Creation

Describes guidelines for exporting grooms as Alembic files for use with Unreal Engine.

![XGen Guidelines for Groom Creation](https://dev.epicgames.com/community/api/documentation/image/8acf91ee-36db-4416-991d-15e8c3458482?resizing_type=fill&width=1920&height=335)

 On this page

This guide will show you how to set up a groom for import from Maya's [legacy XGen hair creation system](http://help.autodesk.com/view/MAYAUL/2018/ENU/?guid=GUID-C6324505-BD4F-4FD2-B340-CF99158D4819) for importing into Unreal Engine with a set of supported attributes outlined in the [Alembic for Grooms Specification](/documentation/en-us/unreal-engine/using-alembic-for-grooms-in-unreal-engine) documentation.

Maya 2018.6 was used in creation of assets for this guide.

## Converting Legacy XGen Descriptions

### Convert Guides to NURBS Curves

Use the following steps to convert your groom's guides to curves in order to save out a set of curves that match the guides you want to transfer.

1. Set Maya's menu set to **Modeling** so that you see the correct menu options available.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ef0abea-b976-413c-b059-0d0e047e8816/menusetselection.png)
2. From the main menu, click the **Generate** dropdown and select **XGen Editor**.
3. In the **XGen** window, use the **Utilities** tab to select **Guides to Curves**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73f53759-f1c7-4509-97a2-66ac72f7184b/xgen_utilities.png)
4. Click **Create Curves**.

Once completed, your groom's output should look similar to this:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/903b034f-8760-4e89-aea7-19110b929ce8/guidestonurbscurvesoutput.png)

### Convert Grooms to XGen Interactive Grooms

If you're using legacy XGen Description, the groom will need to be converted to be an **XGen Interactive Groom**. You can do this by:

1. Select the XGen Description nodes.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74f3a182-7806-4754-9cb0-a9c33fdaaace/xgendescriptionnodes.png)
2. While in the **Modeling** menu set, use the main menu to click the **Generate** dropdown, then select **Convert to Interactive Groom**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3588fa65-fd27-4c64-98bf-4c0a6872bba3/xgeninteractivegroom.png)

## Exporting Spline Descriptions to NURBS Curves

Follow these steps to export your selected spline descriptions as an Alembic file that can be imported with the interpolated hairs as NURBS curves.

1. Select your XGen Spline Description nodes, and while in the **Modeling** menu set, use the main menu to click the **Generate** dropdown. Select **Cache > Export Cache** from the list.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b823244f-4dc2-4275-b2c1-3aa777a503d2/splinedesctonurbscurve_exportcache.png)
2. In the **Export Cache** window, set the following:

   * **Cache Time Frame:** Set to **Current Frame**
   * **Multiple Transforms:** Disabled
   * **Write Final Width:** Enabled![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a0122d2-da90-43a5-a4ec-036a29c14d4c/splinedesctonurbscurve_exportcachewindow.png)
3. Enter a name for your file, and select **Alembic** as the file type.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0330eddc-c142-4f12-b742-1251c8bd0cc9/splinedesctonurbscurve_exportcachefile.png)
4. Click **Export**.
5. Use the **File** menu to select **Import**. This opens the **Import** window, which can be used to select and import your Alembic ('.abc') file into your scene.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15c3a135-09e0-40b4-918e-bdb8dc1dbfe8/splinedesctonurbscurve_importalembic.png)

Once imported, you should now have an XGen Spline Description that was exported and saved as an Alembic file and imported bringing in the interpolated hairs in as NURBS curves.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8eeeb4d8-4f26-4cdc-ad38-f83366d2cb77/splinedesctonurbscurve_output.png)

## Creating Attributes

### Create Group ID Attributes

Interpolated hair can be exported in one or more groups. These groups are recognized in Unreal Engine for unique material assignment.

Use the following script when creating group ID attributes:

```
from maya import cmds

attr_name = 'groom_group_id'

# NOTE: change the following names to reflect your node's scene.
groups = ['hair_brows_splineDescription1|SplineGrp0', 'hair_lashes_splineDescription1|SplineGrp0', 'hair_head_splineDescription1|SplineGrp0']

for groom_group_id, group_name in enumerate(groups):
    
    # get curves under xgGroom
    curves = cmds.listRelatives(group_name, ad=True, type='nurbsCurve')
    
    # tag group with group id
    cmds.addAttr(group_name, longName=attr_name, attributeType='short', defaultValue=groom_group_id, keyable=True)
    
    # add attribute scope
    # forces Maya's alembic to export data as GeometryScope::kConstantScope
    cmds.addAttr(group_name, longName='{}_AbcGeomScope'.format(attr_name), dataType='string', keyable=True)
    cmds.setAttr('{}.{}_AbcGeomScope'.format(group_name, attr_name), 'con', type='string')
Copy full snippet
```

### Create Guide Attributes

When creating the guide attributes for your groom, only the curves tagged as **guide** are used for simulation in Unreal Engine. If there are no guides specified in the Alembic file, a percentage of the interpolated hairs will be internally tagged as guides during the import process into Unreal Engine.

When importing a groom with no guides, the percentage of interpolated hairs that are tagged as guides can be set using the [Groom Import Options](/documentation/en-us/unreal-engine/importing-grooms-into-unreal-engine). By default, only 10% of the number of hairs will be used as guides.

Use the following script when creating your guide attributes:

```
from maya import cmds

attr_name = 'groom_guide'

# get curves under xgGroom
curves = cmds.listRelatives('xgGroom', ad=True, type='nurbsCurve')

# create new group
guides_group = cmds.createNode('transform', name='guides')

# tag group as groom_guide
cmds.addAttr(guides_group, longName=attr_name, attributeType='short', defaultValue=1, keyable=True)

# forces Maya's alembic to export curves as one group.
cmds.addAttr(guides_group, longName='riCurves', attributeType='bool', defaultValue=1, keyable=True)

# add attribute scope
# forces Maya's alembic to export data as GeometryScope::kConstantScope
cmds.addAttr(guides_group, longName='{}_AbcGeomScope'.format(attr_name), dataType='string', keyable=True)
cmds.setAttr('{}.{}_AbcGeomScope'.format(guides_group, attr_name), 'con', type='string')

# parent curves under guides group
for curve in curves:
    cmds.parent(curve, guides_group, shape=True, relative=True)
Copy full snippet
```

#### Groom\_Width Attribute

For Maya, the width value has a special behavior, unlike other DCC applications that can follow the [Alembic for Grooms Specification](/documentation/en-us/unreal-engine/using-alembic-for-grooms-in-unreal-engine) to retrieve them and use them to build the groom.

Maya can export width values directly on the curves so that there's no need to export a custom `groom_width` attribute; the importer converts those values into that attribute automatically. Should the `groom_wdith` attribute be present with the groom during import into Unreal Engine, it is not overwritten. If `groom_wdith` is not specified, or cannot be converted from width values, the builder will fal back on a value of 1 centimeter.

## Export to Alembic from Maya

1. In Maya, select the Guides and Group\_ID curves that you want to export.

   Each node needs to have a unique name.
2. While in the **Modeling** menu set, use the main menu to click the **Cache** dropdown, then select **Alembic Cache > Export Selection to Alembic**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac53eb6c-6d0e-4203-afbd-b72dd6defac0/exporttoalembic_exportselection.png)
3. In the **Export Selection** window, under the **General Options** category, set the **Cache time range** to **Current Frame**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e23c517a-a747-475c-889b-49213bb8c03a/exporttoalembic_exportselection_currentframe.png)
4. Under the **Attributes** category, type the name of the **Attribute** you want to the list and click the **Add** button. Add the following schema attributes:

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9328aa01-54e9-490e-a71b-daa14c6cb3a9/exporttoalembic_exportselection_addattributes.png)
   * groom\_group\_id
   * groom\_guide
5. Enter a file name in the **File name** textbox, and set the **Files of type** to **Alembic**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f1a157b-e3e5-4c04-bb86-aa95ca0d7b2d/exporttoalembic_exportselection_filenametype.png)
6. Click the **Export Selection** button.

## Applying Textures to Hair UVs

The following steps and included script can help you set up your own XGen hair that can be exported to Unreal Engine, and have an applied texture represented on individual hair strands.

1. In Maya use the **Modeling** menu to select **Generate** > **Create Interactive Groom Splines**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2794c6b-bec0-44f2-89dd-482025800461/hairuv_xgen.png)
2. You can create guides and brush the hair as you like for your project. When ready, export the curves as an **Alembic Cache** by selecting **Generate > Cache > Create New Cache**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a73f09c1-895b-48a0-b647-3e9f44f030b4/hairuv_2_xgen.png)
3. Remove your XGen hair by hiding or deleting it. Then, reimport your exported hair curves with your source mesh in the Maya scene.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25606251-64a6-49e2-a261-100a3883c34a/hairuv_3_xgen.png)
4. Depending on your scene, you will have thousands of spline curves parented under a top curve, **SplineGrp0** in this example. Edit the following Python script and replace the following values with the one from your project:

   * export\_directory
   * hair\_file
   * curve\_top\_group
   * uv\_mesh

   You can download the script below [here](https://epicgames.box.com/shared/static/46my2x1sueuc6hlt09ous9czx4o8fhjz.zip).

   ```
    from maya import cmds
    from maya import OpenMaya
    import os

    def create_root_uv_attribute(curves_group, mesh_node, uv_set='map1'):
        '''
        Create "groom_root_uv" attribute on group of curves.
        '''

        # check curves group
        if not cmds.objExists(curves_group):
            raise RuntimeError('Group not found: "{}"'.format(curves_group))

        # get curves in group
        curve_shapes = cmds.listRelatives(curves_group, shapes=True, noIntermediate=True)
        curve_shapes = cmds.ls(curve_shapes, type='nurbsCurve')
        if not curve_shapes:
            raise RuntimeError('Invalid curves group. No nurbs-curves found in group.')
        else:
            print "found curves"
            print curve_shapes

        # get curve roots
        points = list()
        for curve_shape in curve_shapes:
            point = cmds.pointPosition('{}.cv[0]'.format(curve_shape), world=True)
            points.append(point)

        # get uvs
        values = list()
        uvs = find_closest_uv_point(points, mesh_node, uv_set=uv_set)
        for u, v in uvs:
            values.append([u, v, 0])
            #print (str(u) + " , " + str(v)  )

        # create attribute
        name = 'groom_root_uv'
        cmds.addAttr(curves_group, ln=name, dt='vectorArray')
        cmds.addAttr(curves_group, ln='{}_AbcGeomScope'.format(name), dt='string')
        cmds.addAttr(curves_group, ln='{}_AbcType'.format(name), dt='string')

        cmds.setAttr('{}.{}'.format(curves_group, name), len(values), *values, type='vectorArray')
        cmds.setAttr('{}.{}_AbcGeomScope'.format(curves_group, name), 'uni', type='string')
        cmds.setAttr('{}.{}_AbcType'.format(curves_group, name), 'vector2', type='string')

        return uvs

    def find_closest_uv_point(points, mesh_node, uv_set='map1'):
        '''
        Find mesh UV-coordinates at given points.
        '''

        # check mesh
        if not cmds.objExists(mesh_node):
            raise RuntimeError('Node not found: "{}"'.format(mesh_node))

        # check uv_set
        uv_sets = cmds.polyUVSet(mesh_node, q=True, allUVSets=True)
        if uv_set not in uv_sets:
            raise RuntimeError('Invalid uv_set provided: "{}"'.format(uv_set))

        # get mesh as dag-path
        selection_list = OpenMaya.MSelectionList()
        selection_list.add(mesh_node)

        mesh_dagpath = OpenMaya.MDagPath()
        selection_list.getDagPath(0, mesh_dagpath)
        mesh_dagpath.extendToShape()

        # get mesh function set
        fn_mesh = OpenMaya.MFnMesh(mesh_dagpath)

        uvs = list()
        for i in range(len(points)):

            script_util = OpenMaya.MScriptUtil()
            script_util.createFromDouble(0.0, 0.0)
            uv_point = script_util.asFloat2Ptr()

            point = OpenMaya.MPoint(*points[i])
            fn_mesh.getUVAtPoint(point, uv_point, OpenMaya.MSpace.kWorld, uv_set)

            u = OpenMaya.MScriptUtil.getFloat2ArrayItem(uv_point, 0, 0)
            v = OpenMaya.MScriptUtil.getFloat2ArrayItem(uv_point, 0, 1)

            uvs.append((u, v))

        return uvs

    def abc_export(filepath, node=None, start_frame=1, end_frame=1, data_format='otawa', uv_write=True):
           
        job_command = '-frameRange {} {} '.format(start_frame, end_frame)
        job_command += '-dataFormat {} '.format(data_format)
           
        job_command += '-attr groom_root_uv '

        if uv_write:
            job_command += '-uvWrite '
           
        job_command += '-root {} '.format(node)   
           
        job_command += '-file {} '.format(filepath) 
           
        cmds.AbcExport(verbose=True, j=job_command)
                       
    def main():
           
        export_directory = 'D:/Dev/Ref'
        hair_file = os.path.join(export_directory, 'hair_export.abc')
        curve_top_group= 'description1|SplineGrp0'
        uv_mesh='pPlane1'
           
        create_root_uv_attribute( curve_top_group , uv_mesh)
        abc_export(hair_file, curve_top_group)
           
    main()
   Copy full snippet
   ```
5. In Maya, run the script with the changed values to generate a new Alembic ('.abc') file which can be imported into Unreal Engine.
6. In Unreal Engine, create a new Material using the **Hair** Shading Model. In the material graph, add a **Hair Attributes** expression and plug the **Root UV** into the **UV** input of the Texture Sample.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3e6dbec-3203-4d29-ae31-dca854f068e2/hairuv_4_xgen.png)


   The `groom_root_uv` attribute specifies per hair the underlying mesh UV which it is attached to. This attribute is optional, and if not specified, a root UV is automatically generated in the engine using a spherical mapping.
7. Drag your imported hair Alembic file into the level from the Content Browser, and assign your hair material to it. You should end up with something like this:

   Make sure that your hair Alembic file in the level has a width greater than 0.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5238c8e4-9ce7-472e-b63c-4be4414f10d3/hairuv_5_xgen.png)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Converting Legacy XGen Descriptions](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#convertinglegacyxgendescriptions)
* [Convert Guides to NURBS Curves](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#convertguidestonurbscurves)
* [Convert Grooms to XGen Interactive Grooms](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#convertgroomstoxgeninteractivegrooms)
* [Exporting Spline Descriptions to NURBS Curves](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#exportingsplinedescriptionstonurbscurves)
* [Creating Attributes](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#creatingattributes)
* [Create Group ID Attributes](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#creategroupidattributes)
* [Create Guide Attributes](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#createguideattributes)
* [Groom\_Width Attribute](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#groom-widthattribute)
* [Export to Alembic from Maya](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#exporttoalembicfrommaya)
* [Applying Textures to Hair UVs](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine?application_version=5.7#applyingtexturestohairuvs)
