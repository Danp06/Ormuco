def get_resource_id(name,resources):
    for resource in resources:
        if name in resource['name']:
            return resource['id']
    return None

def get_resource_key(name,resources):
    for resource in resources:
        if name in resource['name']:
            return resource['public_key']
    return None

def server_specification(name_image, images, name_network, networks, name_flavor, flavors, 
                         name_keypair, keypairs, name_segurity_group, segurity_groups):
    return {
        'imagen':{
            'name': name_image,
            'id': get_resource_id(name_image,images)
        },
        'network':{
            'name': name_network,
            'id': get_resource_id(name_network,networks)
        },
        'keypair':{
            'name': name_keypair,
            'id': get_resource_key(name_keypair,keypairs)
        },
        'flavor':{
            'name': name_flavor,
            'id': get_resource_id(name_flavor,flavors)
        },
        'security_group':{
            'name': name_network,
            'id': get_resource_id(name_segurity_group,segurity_groups)
        }
    }