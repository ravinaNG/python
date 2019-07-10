def say_hello_languase(name, languase):
	if (languase == "Hindi"):
		print "Namaste", name
		print "Aap kaise ho?"
	elif (languase == "Punjabi"):
		print "Sat ari akaal ", name
		print "Tuada ki haal hai?"
	else:
		print "Hello ", name
		print "How are you?"
say_hello_languase("Rishabh", "Punjabi")
say_hello_languase("Armaan", "English")
say_hello_languase("Abhishek", "french")
say_hello_languase("Sir", "Hindi")
