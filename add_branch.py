# importing libraries
import sys, getopt, argparse

# taking all the arguments except filename which by default is at list_name[0]
argv = sys.argv[1:]

#correct gh org name and project name
c_gh_org_name = "practice"
c_project_slug = 'the_full_proj_slug'
c_new_branch = 'epic-stuff-branch'

#command to parse is:
# set-project-feature "the_full_proj_slug" :pr-only-branch-overrides "develop"

#Dissect the commands we are parsing as follows:
parsed_cmd = ["set-project-feature", "project_slug", ":pr-only-branch-overrides", "develop"]
#print(parsed_cmd[1]) # expecting to print set-project-feature

# write a try catch block
try: 

	#colon means a value is expected
	opts, args = getopt.getopt(argv, "'g':'p':'b':", ['gh_org_name=', 'project_slug=', 'new_branch='])

	print(opts, args)

	if len(opts) != 3:
		print('usage: sample_work.py -g <gh_org_name>  -p <project_slug> -b <new_branch> or ')
		print('usage: sample_work.py --gh_org_name <gh_org_name> --project_slug <project_slug> --new_branch <new_branch>')

	#we need the value for gh_org_name, project_slug and new_branch which we type on the command line
	for opt, arg in opts:
		if opt == '-g' or opt == 'gh_org_name':
			gh_org_name == arg
		elif opt == '-p' or opt == 'project_slug':
			project_slug == arg
		elif opt == '-b' or opt == 'new_branch':
			new_branch == arg 

	# gh_org_name and project_slug verification step
	
	if 'gh_org_name' == c_gh_org_name and 'project_slug' == c_project_slug:
		print("All the information matches as expected!")
	else:
	 	print('The information you entered does not match what is expected please confirm and retype.')

except getopt.GetoptError:
		print('One or more option(s) are not recognized or not in correct format')
		print('usage: sample_work.py -g <gh_org_name>  -p <project_slug> -b <new_branch> or ')
		print('usage: sample_work.py --gh_org_name <gh_org_name> --project_slug <project_slug> --new_branch <new_branch>')


		




