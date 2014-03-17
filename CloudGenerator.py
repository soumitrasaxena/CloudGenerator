import maya.cmds as cmds

class Cloud:
			
	def createCloud(self , *pArgs):
		
		self.cloudList = cmds.ls(selection = True)
		self.cloudShape = cmds.listRelatives(self.cloudList , c=True)
		self.w = 20
		self.h = 1
		self.d = 20
		self.transparency = 0.125
		self.edgeDropoff = 0.165
		self.frequency = 4.126
		
				
		cmds.setAttr(self.cloudShape[0]+'.squareVoxels' , 0)
		cmds.setAttr(self.cloudShape[0]+'.resolution' , 80,4,80)
		cmds.setAttr(self.cloudShape[0]+'.dimensions' , self.w,self.h,self.d)
		cmds.setAttr(self.cloudShape[0]+'.densityMethod' , 0)
		cmds.setAttr(self.cloudShape[0]+'.velocityMethod' , 0)
		cmds.setAttr(self.cloudShape[0]+'.transparency' , self.transparency , self.transparency , self.transparency , type = 'double3')
		cmds.setAttr(self.cloudShape[0]+'.edgeDropoff' , self.edgeDropoff)
		cmds.setAttr(self.cloudShape[0]+'.color[0].color_Position' ,0)
		cmds.setAttr(self.cloudShape[0]+'.color[0].color_Color' , 1 , 0.904 , 0.815)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Position' , 0.214)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Color' , 0.2,0.263,0.338)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Position' , 0.421)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Color' , 0.138,0.194,0.331)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Position' , 0.650)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Color' , 0.023,0.094,0.121)
		
		cmds.setAttr(self.cloudShape[0]+'.incandescenceInput' , 2)
		cmds.setAttr(self.cloudShape[0]+'.opacity[0].opacity_Position' , 0.379)
		cmds.setAttr(self.cloudShape[0]+'.opacity[0].opacity_FloatValue' , 0)
		
		cmds.setAttr(self.cloudShape[0]+'.opacity[1].opacity_Position' , 0.436)
		cmds.setAttr(self.cloudShape[0]+'.opacity[1].opacity_FloatValue' , 0.020)
		cmds.setAttr(self.cloudShape[0]+'.opacity[1].opacity_Interp' , 1)
		
		cmds.setAttr(self.cloudShape[0]+'.opacity[2].opacity_Position' , 0.479)
		cmds.setAttr(self.cloudShape[0]+'.opacity[2].opacity_FloatValue' , 0.360)
		cmds.setAttr(self.cloudShape[0]+'.opacity[2].opacity_Interp' , 1)
		
		
		cmds.setAttr(self.cloudShape[0]+'.opacity[3].opacity_Position' , 0.593)
		cmds.setAttr(self.cloudShape[0]+'.opacity[3].opacity_FloatValue' , 0.6)
		cmds.setAttr(self.cloudShape[0]+'.opacity[3].opacity_Interp' , 1)
		
		
		cmds.setAttr(self.cloudShape[0]+'.opacity[4].opacity_Position' , 0.8)
		cmds.setAttr(self.cloudShape[0]+'.opacity[4].opacity_FloatValue' , 0.82)
		cmds.setAttr(self.cloudShape[0]+'.opacity[4].opacity_Interp' , 1)
		
		
		cmds.setAttr(self.cloudShape[0]+'.opacity[5].opacity_Position' , 1)
		cmds.setAttr(self.cloudShape[0]+'.opacity[5].opacity_FloatValue' , 0.940)
		cmds.setAttr(self.cloudShape[0]+'.opacity[5].opacity_Interp' , 1)
		
		cmds.setAttr(self.cloudShape[0]+'.opacityInput' , 2)
		cmds.setAttr(self.cloudShape[0]+'.opacityInputBias' , 0.152)
		
		cmds.setAttr(self.cloudShape[0]+'.incandTexture' , 1)
		cmds.setAttr(self.cloudShape[0]+'.opacityTexture' , 1)
		
		cmds.setAttr(self.cloudShape[0]+'.opacityTexGain' , 1.126)
		cmds.setAttr(self.cloudShape[0]+'.amplitude' , 0.981)
		cmds.setAttr(self.cloudShape[0]+'.ratio' , 0.427)
		cmds.setAttr(self.cloudShape[0]+'.frequencyRatio' , 2.2)
		cmds.setAttr(self.cloudShape[0]+'.depthMax' , 4)
		
		cmds.setAttr(self.cloudShape[0]+'.inflection' , 1)
		cmds.setAttr(self.cloudShape[0]+'.frequency' , self.frequency)
		
		cmds.setAttr(self.cloudShape[0]+'.selfShadowing' , 1)
		cmds.setAttr(self.cloudShape[0]+'.shadowOpacity' , 0.718)
		
		cmds.setAttr(self.cloudShape[0]+'.realLights', 0)
		cmds.setAttr(self.cloudShape[0]+'.directionalLight' , 0.5 , 0.140 , -4)
	
	def updateSize(self):
		cmds.setAttr(self.cloudShape[0]+'.dimensions' , self.w,self.h,self.d)
	
	def setW(self , w):
		self.w = w
		self.updateSize()
	
	def setH(self , h):
		self.h = h
		self.updateSize()
	
	def setD(self , d):
		self.d = d
		self.updateSize()
		
	def setTransparency(self , transparency):
		self.transparency = transparency
		cmds.setAttr(self.cloudShape[0]+'.transparency' , self.transparency , self.transparency , self.transparency , type = 'double3')
		
		
	def setEdgeDropoff(self , ed):
		self.edgeDropoff = ed
		cmds.setAttr(self.cloudShape[0]+'.edgeDropoff' , self.edgeDropoff);
	
	def setFrequency(self , fr):
		self.frequency = fr
		cmds.setAttr(self.cloudShape[0]+'.frequency' , self.frequency);
		print self.frequency
	
	def day(self , *pArgs):
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Position' , 0.214)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Color' , 1,1,1)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Position' , 0.421)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Color' , 0.442,0.584,0.747)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Position' , 0.650)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Color' , 0.120,0.493,0.629)
		
	
	def sunset(self , *pArgs):
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Position' , 0.214)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Color' , 0.2,0.263,0.338)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Position' , 0.421)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Color' , 0.138,0.194,0.331)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Position' , 0.650)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Color' , 0.023,0.094,0.121)
		
	
	def night(self , *pArgs):
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Position' , 0.214)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[0].incandescence_Color' , 0,0,0)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Position' , 0.421)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[1].incandescence_Color' , 0.03,0.043,0.073)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Position' , 0.650)
		cmds.setAttr(self.cloudShape[0]+'.incandescence[2].incandescence_Color' , 0,0,0)
		
		
		
def createUI( pWindowTitle , cloud):
	
	windowID = 'myWindowID'
	
	if cmds.window(windowID , exists = True):
		cmds.deleteUI(windowID)
		
	cmds.window(windowID , title = pWindowTitle , sizeable = False , resizeToFitChildren = True)
	
	cmds.rowColumnLayout( numberOfColumns = 3 , columnWidth =[(1,200) , (2,200) , (3 ,200)] , columnOffset = (1 , 'right' , 5))
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.button(label = 'Generate Cloud' , command = cloud.createCloud )
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.text(label = 'Set The Size of the Clouds')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.text(label = 'Set Width')
	
	cmds.intSlider(min = 0 , max = 100 , value = 20 , step = 1 , w = 200 , dragCommand = lambda w : cloud.setW(w))
	
	cmds.separator ( h = 10 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.text(label = 'Set Height')
	
	cmds.intSlider(min = 0 , max = 100 , value = 20 , step = 1 , w = 200 , dragCommand = lambda h : cloud.setH(h))
	
	cmds.separator ( h = 10 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	
	cmds.text(label = 'Set Depth')
	
	cmds.intSlider(min = 0 , max = 100 , value = 20 , step = 1 , w = 200 , dragCommand = lambda d : cloud.setD(d))
	
	cmds.separator ( h = 10 , style = 'none')
	cmds.separator ( h = 50 , style = 'none')
	cmds.separator ( h = 50 , style = 'none')
	cmds.separator ( h = 50 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.text(label = 'Set How the Clouds Look')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	
	cmds.text(label = 'Density of Clouds')
	
	cmds.floatSlider(min = 0 , max = 1 , value = 0.125 , step = 0.001, w = 200 , dragCommand = lambda t : cloud.setTransparency(t))
	
	cmds.separator ( h = 10 , style = 'none')
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.text(label = 'Increase to Centralize Clouds')
	
	cmds.floatSlider(min = 0 , max = 1 , value = 0.165 , step = 0.001, w = 200 , dragCommand = lambda ed : cloud.setEdgeDropoff(ed))
	
	cmds.separator ( h = 10 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.text(label = 'Set Size of Clouds ( reduces Number ) ')
	
	cmds.floatSlider(min = 0 , max = 5 , value = 4.126 , step = 0.01, w = 200 , dragCommand = lambda fr : cloud.setFrequency(fr))
	
	cmds.separator ( h = 10 , style = 'none')	
	
	
	cmds.separator ( h = 50 , style = 'none')
	cmds.text(label = 'Select the Time of the Day')
	cmds.separator ( h = 50 , style = 'none')
	
	cmds.radioCollection()
	
	cmds.radioButton( label='Day', align='center' , onCommand = cloud.day )
	cmds.radioButton( label='Sunset', align='right' , onCommand = cloud.sunset )
	cmds.radioButton( label='Night', align='center' , onCommand = cloud.night )
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.button(label = 'Reset To Default' , command = cloud.createCloud )
	cmds.separator ( h = 20 , style = 'none')	
		
	cmds.showWindow()
	
newcloud = Cloud()
createUI('Cloud Generator 1.0' , newcloud)