import globalVars
from displayModel import DisplayModelTextInfo
from NVDAObjects.IAccessible import IAccessible 
import _default
import ui
import api
import textInfos
import controlTypes

class AppModule(_default.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_WINDOW: return
		if obj.windowClassName == "AfxFrameOrView42s" and obj.role == controlTypes.ROLE_PANE:
			clsList.insert(0, OutputWindow)
	def script_moveToOutput(self, keyPress):
		"""moves to the bottom of the output window, silently."""
		obj = api.getFocusObject()
		if obj.windowClassName != 'Edit':
			ui.message("not in edit window")
			return
		#try to go up the parent tree to find the client. Confirm, and find the child.
		p = obj.parent.parent
		if p.windowClassName != 'AfxMDIFrame42s':
			ui.message("unable to find MDI client")
			return
		obj = p.children[0]
#		api.setNavigatorObject(obj)
		info = obj.makeTextInfo(textInfos.POSITION_LAST)
		api.setReviewPosition(info)

class OutputWindow(IAccessible):
	role = controlTypes.ROLE_TERMINAL
	TextInfo = DisplayModelTextInfo