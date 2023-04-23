import digitalocean

with open('token.env') as fin:
	PRIVATE_TOKEN = fin.read().rstrip()


manager = digitalocean.Manager(token=PRIVATE_TOKEN)
my_projects = manager.get_all_projects()

try:
	disposable_project = next(p for p in my_projects if p.name == 'Disposable Droplets')
except StopIteration:
	# make a new project for disposable droplets
	print('Create a new project called "Disposable Droplets"')
	exit()


new_droplet = digitalocean.Droplet(token = PRIVATE_TOKEN,
								   name = 'test',
								   region = 'nyc1',
								   image = 'debian-11-x64',
								   size_slug = 's-1vcpu-1gb')