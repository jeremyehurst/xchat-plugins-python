import xchat
__module_name__ = "massinv" 
__module_version__ = "0.2" 
__module_description__ = "Mass inviter by xanax" 

print "\0034",__module_name__, __module_version__," loaded\000"

def massinv(word, word_eol, userdata):
    try:
		users = xchat.get_list("users")
		for user in users:
			xchat.command("INVITE %s %s" % (user.nick, word_eol[1]))
    except:
        print "Usage: /massinv <#channel>" 
    return xchat.EAT_ALL
xchat.hook_command("massinv", massinv, help="/massinv <#channel> :Invites entire current channel to <#channel>") 
	
	
