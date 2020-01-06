MUSHclient NVDA plugin readme

Installation instructions:
1. Put the two .dll files that came in the archive in the MUSHclient program directory.
2. Put the plugin (tts_nvda.xml) in your plugins directory, or somewhere where it won't accidentally get deleted. Usually this is in worlds\plugins off the program directory.
3. Start MUSHclient. Go into global options (control alt g, or in the file menu) and check allow loading of dll's on the lua tab. Either edit the
sandbox to trust all worlds and trust the NVDA plugin, or just replace the entire thing with -- (two minus signs) to disable it. Note that control+a won't work in this edit field; press control-home, control-shift-end, --.
4. There are two ways of loading this plugin. You can either add it globally to all worlds on the plugins tab of the global preferences, or use the plugin dialog inside each world to load it in each world you create. Just go to add, and select the tts_nvda.xml file wherever you put it.

In order to read the output area, You'll need a recent NVDA snapshot (r3508 or above, as of 2010-05-14). Put the mushclient.py and mushclient_desktop.kbd files in your appModules folder in your userconfig directory. Usually this is %appdata%\nvda on non-portable versions and <portablePath>\userConfig in portable builds.
Once this is done, nvda+enter will become the key that moves the navigator to the last line of the output window. Yes, I realize this conflicts with the default action script. If this is a problem, you can change this key to something else by editing the .kbd file. This was done for ease of review on the laptop layout; it is possible to hold down caps lock and review away while easily getting to the bottom to reverse read new output.

If you want to recompile this dll, you'll need PureBasic, the lua libs and includes. The
forum post for the includes is at:
http://www.purebasic.fr/english/viewtopic.php?p=127487
The libs can be found at http://luabinaries.sf.net.

Improvements and suggestions are welcome. My contact info is at the end of the file.

Tyler Spivey
Email: tspivey@pcdesk.net
Twitter: tspivey
