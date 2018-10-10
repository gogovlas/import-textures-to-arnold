import maya.cmds as cmds

vars = {
"path": None,
"target": {"All": None, "Selected": None},
"mapPrefix": None,
"mapSuffix": None,
"imageType": None,
"meshSuffix": "",
"sample": None,
"maps": {"Color": {"Enabled": None, "ID": None}, "Metalness": {"Enabled": None, "ID": None}, "Specular": {"Enabled": None, "ID": None}, "Normal": {"Enabled": None, "ID": None}}
}

#************************* HOME CARD *************************#
def home_Card():
	cmds.rowLayout(numberOfColumns=3)
	cmds.text('Path: ')
	global vars
	vars["path"] = cmds.textField(w=540)
	cmds.button(label='...', command='setPath()',w=62)
	cmds.setParent('..')
	
	cmds.rowLayout(numberOfColumns=2)
	cmds.text('Map prefix: ')
	vars["mapPrefix"] = cmds.textField(w=150, cc="update()")
	cmds.setParent('..')
	
	cmds.rowLayout(numberOfColumns=2)
	cmds.text('Map suffix: ')
	vars["mapSuffix"] = cmds.textField(w=150, cc="update()")
	cmds.setParent('..')
	
	cmds.rowLayout(numberOfColumns=2)
	cmds.text('Image type: .')
	vars["imageType"] = cmds.textField(tx='jpg', w=30, cc="update()")
	cmds.setParent('..')
	
	cmds.rowLayout()
	cmds.text(" ")
	cmds.setParent('..')
	
	cmds.rowLayout( numberOfColumns=3 )
	cmds.text("Target object(s): ")
	cmds.radioCollection()
	vars["target"]["Selected"] = cmds.radioButton( label='Selected', sl=True, cc="update()" )
	vars["target"]["All"] = cmds.radioButton( label='All', cc="update()" )
	cmds.setParent('..')
	
	cmds.rowLayout()
	cmds.text(" ")
	cmds.setParent('..')
	
   	cmds.rowLayout( numberOfColumns=2 )
   	cmds.text("Example")
   	cmds.text(" ")
   	cmds.setParent('..')
   	
   	cmds.rowLayout( numberOfColumns=2 )
   	cmds.text("object:")
   	cmds.text("torso", font = "obliqueLabelFont")
   	cmds.setParent('..')
   	
   	cmds.rowLayout( numberOfColumns=2 )
   	cmds.text("texture:")	
	vars['sample'] = cmds.text("torso_BaseColor.jpg", font = "obliqueLabelFont")
	cmds.setParent('..')
	
	cmds.rowLayout()
	cmds.text(" ")
	cmds.setParent('..')
	
	cmds.rowLayout()
	cmds.button(label="Import", command="importTextures()")
	cmds.setParent('..')
	cmds.setParent('..')

#************************* ADVANCED CARD *************************#
def advanced_Card():
    global vars
    cmds.rowLayout(numberOfColumns=2)
    vars["maps"]["Color"]["Enabled"] = cmds.checkBox( label='Color', v=1, cc="cmds.textField(vars['maps']['Color']['ID'], e=True, en=cmds.checkBox(vars['maps']['Color']['Enabled'], q=1, v=1))")
    vars["maps"]["Color"]["ID"] = cmds.textField(tx='_BaseColor', w=150, cc="update()")
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns=2)
    vars["maps"]["Metalness"]["Enabled"] = cmds.checkBox( label='Metalness', v=1, cc="cmds.textField(vars['maps']['Metalness']['ID'], e=True, en=cmds.checkBox(vars['maps']['Metalness']['Enabled'], q=1, v=1))")
    vars["maps"]["Metalness"]["ID"] = cmds.textField(tx='_Metalness', w=150, cc="update()")
    cmds.setParent('..')
    
    cmds.rowLayout(numberOfColumns=2)
    vars["maps"]["Specular"]["Enabled"] = cmds.checkBox( label='Specular', v=1, cc="cmds.textField(vars['maps']['Specular']['ID'], e=True, en=cmds.checkBox(vars['maps']['Specular']['Enabled'], q=1, v=1))")
    vars["maps"]["Specular"]["ID"] = cmds.textField(tx='_Roughness', w=150, cc="update()")
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns=2)
    vars["maps"]["Normal"]["Enabled"] = cmds.checkBox( label='Normal', v=1, cc="cmds.textField(vars['maps']['Normal']['ID'], e=True, en=cmds.checkBox(vars['maps']['Normal']['Enabled'], q=1, v=1))")
    vars["maps"]["Normal"]["ID"] = cmds.textField(tx='_Normal', w=150, cc="update()")
    cmds.setParent('..')

#print cmds.textField(cTF, e=True, en=cmds.checkBox(cCB, q=1, v=1))

#************************* HELP CARD *************************#
def help_Card():
	cmds.text("\nImport Textures for Arnold\n", font = "boldLabelFont")
	
	cmds.text("      1. Export texture maps from your software of choice. Use consistent naming", al='left')
	cmds.text("      2. Specify the fields in Home tab and Advanced tab to identify the textures", al='left')
	cmds.text("      3. Choose your target object(s), to look for textures for all or only for the selected objects in the scene", al='left')
	cmds.text("      4. Use the Advanced tab to choose what maps to import and how to identify them.\n          By default these are set to the Ai Standard Surface naming conventions", al='left')
	cmds.text("      5. Press Import", al='left')
	
	cmds.text("\n\nby Vlasis Gogousis",al='center', font = "obliqueLabelFont")
	cmds.text("vgogousis@gmail.com",al='center', font = "obliqueLabelFont")
	cmds.text("\nSeptember 2018",al='center', font = "obliqueLabelFont")

#************************* GUI WINDOW *************************#
# Set dimension and name for the window
cWindow = cmds.window(title="Import Textures for Arnold", height = 180, width = 640,sizeable=False)

# Define somes tabs and format of them
tabs = cmds.tabLayout(innerMarginWidth=5,innerMarginHeight=5)

# Insert home card
Home = cmds.columnLayout(adj=True)
home_Card()

AdvancedCard = cmds.columnLayout(adj=True)
advanced_Card()
cmds.setParent('..')

# Insert help card
HelpCard = cmds.columnLayout(adj=True)
help_Card()

# Set column hierarchy
cmds.setParent('..')
cmds.setParent('..')


# Set tab layout and name tabs
cmds.tabLayout(tabs,edit=True,tabLabel=((Home,"Home"),(AdvancedCard,"Advanced"),(HelpCard,"Info")))
cmds.showWindow(cWindow)


def setPath():
    p = cmds.fileDialog2(fm=2, okc="Set")
    global vars
    cmds.textField(vars['path'], e = True, tx = p[0] + '/')
    update()

 
def update():
    global vars
    path = cmds.textField(vars['path'], q=1, tx=1)
    meshSuffix = vars['meshSuffix']
    mapPrefix = cmds.textField(vars['mapPrefix'], q=1, tx=1)
    mapSuffix = cmds.textField(vars['mapSuffix'], q=1, tx=1)
    imageType = cmds.textField(vars['imageType'], q=1, tx=1)
    mapID = cmds.textField(vars['maps']['Color']['ID'], q=1, tx=1)

    sample = path + mapPrefix + "torso" + mapSuffix + mapID + '.' + imageType
    cmds.text(vars['sample'], e=True, l = sample)


def importTextures():
    global vars
    
    path = cmds.textField(vars['path'], q=1, tx=1)
    meshSuffix = vars['meshSuffix']
    mapPrefix = cmds.textField(vars['mapPrefix'], q=1, tx=1)
    mapSuffix = cmds.textField(vars['mapSuffix'], q=1, tx=1)
    imageType = cmds.textField(vars['imageType'], q=1, tx=1)
    
    maps = {}
    for mp in vars['maps']:
        en = cmds.checkBox(vars['maps'][mp]['Enabled'], q=1, v=1)
        id = cmds.textField(vars['maps'][mp]['ID'], q=1, tx=1)
        maps[mp] = {'Enabled': en, 'ID': id}
        #print maps[mp]
    
    missingTextures = []

    meshList = {False: cmds.listRelatives(cmds.ls(g=True), p=True, pa=True), True: cmds.ls(sl = True)}[cmds.radioButton(vars["target"]["Selected"], q=1, sl=1)]
    
    window = cmds.window()
    cmds.columnLayout()
    progressControl = cmds.progressBar(maxValue=len(meshList), width=300)
    cmds.showWindow(window) 

    for mesh in meshList:

        mesh = {0: mesh}.get(len(meshSuffix), mesh[:-len(meshSuffix)]) # remove suffix if applicable
        material = mesh + "_Mtl" #create a material for selected mesh
        print '============================================================'
        print 'Creating material: ' + material + '...'
        print '============================================================'
        cmds.shadingNode('aiStandardSurface', asShader=True, name=material) #plus a shading node
        cmds.sets(renderable=True,  noSurfaceShader=True, empty=True, name= material + "_SG")
        cmds.connectAttr(material + '.outColor', material + '_SG.surfaceShader', force=True)
        cmds.select(mesh)
        cmds.hyperShade(assign=material)

        print " "
        
        if maps['Color']['Enabled']:
            textureFile = path + mapPrefix + mesh + mapSuffix + maps['Color']['ID'] + "." + imageType
            if cmds.file( textureFile, q=True, ex=True ):
                connectMap(textureFile, material, 'Color')
            else:
                missingTextures.append(textureFile)
        if maps['Metalness']['Enabled']:
            textureFile = path + mapPrefix + mesh + mapSuffix + maps['Metalness']['ID'] + "." + imageType        
            if cmds.file( textureFile, q=True, ex=True ):
                connectMap(path + mapPrefix + mesh + mapSuffix + maps['Metalness']['ID'] + "." + imageType, material, 'Metalness')
            else:
                missingTextures.append(textureFile)
        if maps['Specular']['Enabled']:
            textureFile = path + mapPrefix + mesh + mapSuffix + maps['Specular']['ID'] + "." + imageType
            if cmds.file( textureFile, q=True, ex=True ):
                connectMap(path + mapPrefix + mesh + mapSuffix + maps['Specular']['ID'] + "." + imageType, material, 'Specular')
            else:
                missingTextures.append(textureFile)
        if maps['Normal']['Enabled']:
            textureFile = path + mapPrefix + mesh + mapSuffix + maps['Normal']['ID'] + "." + imageType
            if cmds.file( textureFile, q=True, ex=True ):
                connectMap(path + mapPrefix + mesh + mapSuffix + maps['Normal']['ID'] + "." + imageType, material, 'Normal')
            else:
                missingTextures.append(textureFile)

        cmds.progressBar(progressControl, edit=True, step=1)

    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.refresh()
    cmds.toggleWindowVisibility(window)
    
    msg=""
   
    if len(missingTextures)!=0:
        msg = msg + missingTextures[0] + '\n'
        for mt in missingTextures[1:]:
            msg = msg + mt + '\n'
        displayMissing(msg)
    
def displayMissing(msg):
    ww = cmds.window(title="Error Opening Files...", height = 240, width = 820,sizeable=False)
    cmds.columnLayout( )
    cmds.text("\nOops! Couldn't find the following texture files:\n")
    def fClose(*_):
        cmds.deleteUI(ww)
    cmds.scrollField( editable=False, wordWrap=False, text=msg, w=810, h=200 )
    cmds.button(l='Dismiss', w=80, h=30, c=fClose)
    cmds.showWindow(ww) 

#connectMap(path + mapPrefix + mesh + mapSuffix + maps['Color']['ID'] + "." + imageType, material, 'Color')

def connectMap(filePath, material, type):
    if type=='Color':
        colorMap(filePath, material)
    elif type=='Metalness':
        metalnessMap(filePath, material)
    elif type=='Specular':
        specularMap(filePath, material)
    else:
        normalMap(filePath, material)
        
def colorMap(filePath, material):
    # if a file texture is already connected to this input, update it
    # otherwise, delete it
    input = 'baseColor'
    colorSpace = 'sRGB'
    
    # no connected file texture, so make a new one
    newFile = cmds.shadingNode('file',asTexture=1,icm=True)
    newPlacer = cmds.shadingNode('place2dTexture',asUtility=1,icm=True)
    # make common connections between place2dTexture and file texture
    connections = ['rotateUV','offset','noiseUV','vertexCameraOne','vertexUvThree','vertexUvTwo','vertexUvOne','repeatUV','wrapV','wrapU','stagger','mirrorU','mirrorV','rotateFrame','translateFrame','coverage']
    cmds.connectAttr(newPlacer+'.outUV',newFile+'.uvCoord')
    cmds.connectAttr(newPlacer+'.outUvFilterSize',newFile+'.uvFilterSize')
    for i in connections:
        cmds.connectAttr(newPlacer+'.'+i,newFile+'.'+i)
    # now connect the file texture output to the material input
    print 'Connecting color map...'
    cmds.connectAttr(newFile+'.outColor',material+'.'+input,f=1)
    print '>> ' +  newFile+'.outColor' + ' connected to ' + material+'.'+input
    cmds.setAttr(newFile+'.alphaIsLuminance',0)
    print '>> ' +  newFile+'.alphaIsLuminance set to 0'
    
    cmds.setAttr(newFile+'.fileTextureName',filePath,type='string')
    cmds.setAttr(newFile+'.cs',colorSpace,type='string')
    print '>> ' +  newFile+'.cs set to ' + colorSpace
    print " "
        
def metalnessMap(filePath, material):
    # if a file texture is already connected to this input, update it
    # otherwise, delete it
    input = 'metalness'
    colorSpace = 'Raw'
    
    # no connected file texture, so make a new one
    newFile = cmds.shadingNode('file',asTexture=1,icm=True)
    newPlacer = cmds.shadingNode('place2dTexture',asUtility=1,icm=True)
    # make common connections between place2dTexture and file texture
    connections = ['rotateUV','offset','noiseUV','vertexCameraOne','vertexUvThree','vertexUvTwo','vertexUvOne','repeatUV','wrapV','wrapU','stagger','mirrorU','mirrorV','rotateFrame','translateFrame','coverage']
    cmds.connectAttr(newPlacer+'.outUV',newFile+'.uvCoord')
    cmds.connectAttr(newPlacer+'.outUvFilterSize',newFile+'.uvFilterSize')
    for i in connections:
        cmds.connectAttr(newPlacer+'.'+i,newFile+'.'+i)
    print 'Connecting metalness map...'
    cmds.connectAttr(newFile + '.outAlpha',material+'.'+input,f=1)
    print '>> ' + newFile+'.outAlpha' + ' connected to ' + material+'.'+input
    cmds.setAttr(newFile+'.alphaIsLuminance',1)
    print '>> ' + newFile + '.alphaIsLuminance set to 1'
        
    cmds.setAttr(newFile+'.fileTextureName',filePath,type='string')
    cmds.setAttr(newFile+'.cs',colorSpace,type='string')
    print '>> ' +  newFile+'.cs set to ' + colorSpace
    print " "
    
def specularMap(filePath, material):
    # if a file texture is already connected to this input, update it
    # otherwise, delete it
    input = 'specularRoughness'
    colorSpace = 'Specular'
    
    # no connected file texture, so make a new one
    newFile = cmds.shadingNode('file',asTexture=1,icm=True)
    newPlacer = cmds.shadingNode('place2dTexture',asUtility=1,icm=True)
    # make common connections between place2dTexture and file texture
    connections = ['rotateUV','offset','noiseUV','vertexCameraOne','vertexUvThree','vertexUvTwo','vertexUvOne','repeatUV','wrapV','wrapU','stagger','mirrorU','mirrorV','rotateFrame','translateFrame','coverage']
    cmds.connectAttr(newPlacer+'.outUV',newFile+'.uvCoord')
    cmds.connectAttr(newPlacer+'.outUvFilterSize',newFile+'.uvFilterSize')
    for i in connections:
        cmds.connectAttr(newPlacer+'.'+i,newFile+'.'+i)
    print 'Connecting specular map...'
    cmds.connectAttr(newFile + '.outAlpha',material+'.'+input,f=1)
    print '>> ' + newFile+'.outAlpha' + ' connected to ' + material+'.'+input
    cmds.setAttr(newFile+'.alphaIsLuminance',1)
    print '>> ' + newFile + '.alphaIsLuminance set to 1'
        
    cmds.setAttr(newFile+'.fileTextureName',filePath,type='string')
    cmds.setAttr(newFile+'.cs',colorSpace,type='string')
    print '>> ' +  newFile+'.cs set to ' + colorSpace
    print " "


def normalMap(filePath, material):
    # if a file texture is already connected to this input, update it
    # otherwise, delete it
    input = 'normalCamera'
    colorSpace = 'Raw'
    
    # no connected file texture, so make a new one
    newFile = cmds.shadingNode('file',asTexture=1,icm=True)
    newPlacer = cmds.shadingNode('place2dTexture',asUtility=1,icm=True)
    # make common connections between place2dTexture and file texture
    connections = ['rotateUV','offset','noiseUV','vertexCameraOne','vertexUvThree','vertexUvTwo','vertexUvOne','repeatUV','wrapV','wrapU','stagger','mirrorU','mirrorV','rotateFrame','translateFrame','coverage']
    cmds.connectAttr(newPlacer+'.outUV',newFile+'.uvCoord')
    cmds.connectAttr(newPlacer+'.outUvFilterSize',newFile+'.uvFilterSize')
    for i in connections:
        cmds.connectAttr(newPlacer+'.'+i,newFile+'.'+i)
    print 'Connecting normal map...'
    bumpNode = cmds.shadingNode('bump2d',asUtility=1,icm=True)
    cmds.connectAttr(newFile + '.outAlpha', bumpNode + '.bumpValue',f=1)
    cmds.connectAttr( bumpNode + '.outNormal', material + '.' + input, f=1)
    cmds.setAttr (bumpNode + '.bumpInterp', 1)
    print '>> ' +  newFile+' set to tangent space normals'
    cmds.setAttr (bumpNode + '.aiFlipG', 0)
    print '>> ' +  newFile+'.FlipRG set to 0'
    cmds.setAttr (bumpNode + '.aiFlipR', 0)
    cmds.setAttr(newFile+'.alphaIsLuminance',0)
    print '>> ' +  newFile+'.alphaIsLuminance set to 0'
        
    cmds.setAttr(newFile+'.fileTextureName',filePath,type='string')
    cmds.setAttr(newFile+'.cs',colorSpace,type='string')
    print '>> ' +  newFile+'.cs set to ' + colorSpace
    print " "
