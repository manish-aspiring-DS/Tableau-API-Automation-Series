# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 03:12:13 2023

@author: Pandas Analytics Hub   ||   Email : p.analyticshub@gmail.com   || Mobile : +91-9774083186

"""

# =============================================================================
# Importing of modules
# =============================================================================

import tableauserverclient as TSC

# =============================================================================
# Variable Initialization
# =============================================================================

serv='https://prod-apnortheast-a.online.tableau.com'
uname='p.analyticshub@gmail.com'
pwd='Pandas@123'
site='pah'  # If site is Default then leave it blank else pass the site name


# Creating a tableau authentication object 
tableau_auth = TSC.TableauAuth(uname, pwd, site)
server = TSC.Server(serv, use_server_version=True)

# This will ignore the SSL certificate check(use this only if tableau server has SSL configured)
# This should always be used with tableau online as it is SSL configured by default 
server.add_http_options({'verify': False})

#Sign in in tableau online / server 
server.auth.sign_in(tableau_auth)

# Getting the list of users on tableau online
print(server.users.get())

server.auth.sign_out()

