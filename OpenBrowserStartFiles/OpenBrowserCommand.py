''' :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Developer 	: Gianpiere Julio Ramos Bernuy
	Contact		: gianpiere@live.com
	Description : funcion que permite ejecutar en el navegador los routes de codeigniter que selecciones

	{ "keys": ["ctrl+shift+b"], "command": "open_browser","args": {"block":true,"url_basepath":"http://urlbase/"}}

	keymap que activa el API. 
	---------------------------------------------------------------------------------------------------------------
''' 
import sublime, sublime_plugin
import webbrowser
import urllib
import re, os, os.path
# { "keys": ["ctrl+shift+b"], "command": "open_browser","args": {"block":true,"url_basepath":"http://urlbase/"}}
# STx64 GRB/Data/Packages/User/OpenBrowserStartFiles.sublime-settings
class OpenBrowserCommand(sublime_plugin.TextCommand):
	
	def run(self,edit,block,url_basepath,author):
		window = sublime.active_window()
		view = self.view
		self.settings = sublime.load_settings("OpenBrowserStartFiles.sublime-settings")
		settings_pkg = self.settings.get("Parametros")

		user_name = settings_pkg[0]["Nombre"]
		css_package = settings_pkg[1]["css"]
		js_package = settings_pkg[2]["js"]

		view = self.view

		selection_region = view.sel()[0]
		word_region = view.word(selection_region)
		word = view.substr(word_region).strip()
		word = re.sub('[\(\)\{\}\s]', '', word)

		window = sublime.active_window()
		proj_folders = window.folders()

		if author != 'gianpiere@live.com':
			print("author: gianpiere@live.com no ha sido asignado.")
			#sublime.message_dialog(sublime.get_clipboard())
			return 0
		if url_basepath == '':
			url_basepath = 'http://localhost/'
		for region in self.view.sel():
			t = self.view.substr(region)
			if not region.empty():
				result = self.view.file_name().split('\\')
				
				if str(type(result)) == "<class 'list'>":
					if result[-1] == 'routes.php':
						text = self.view.substr(region)
						url = url_basepath+text
						webbrowser.open_new(url)
					else:
						text = self.view.substr(region)
						subresult = text.split('.')
						if str(type(subresult)) == "<class 'list'>":
							if subresult[-1] == 'css':
								print(result[0])
								window.open_file(result[0]+'\\'+css_package+text, sublime.ENCODED_POSITION)
							elif subresult[-1] == 'js':
								window.open_file(result[0]+'\\'+js_package+text, sublime.ENCODED_POSITION)
							elif subresult[-1] != '':
								self.view.window().run_command("show_overlay", {"overlay": "goto", "text": text})
								#self.view.window().run_command("show_panel",{"panel": "find_in_files","text":'asdasds '+text})
							else:
								print('No File Correct')
						else:
							print('No ha Seleccionado un Archivo Valido [CSS, JS]')
			else:
				url = url_basepath
				webbrowser.open_new(url)


	

''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '::' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '::' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 