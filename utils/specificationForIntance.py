def loop(lista):
    for i in lista:
        return i

def get_resource_id(name,resources):
    for resource in resources:
        if name in resource['name']:
            return resource['id']
    return None

def get_resource(name,resources):
    for resource in len(resources):
        if name in resource['id']:
            return resource
    return None

def get_resource_key(name,resources):
    for resource in resources:
        if name in resource['name']:
            return resource['public_key']
    return None

def get_ipDown(resources):
    for resource in resources:
        if 'DOWN' in resource['status']:
            return resource['floating_ip_address']
    return None


def server_specification(data):
    namei = 'ubuntu-18'
    namen = 'default'
    namekey = 'Daniel_Pena'
    namefla = 'general.pico.uat.linux'
    namesecu = 'web'
    return {
        'imagen':{
            'name': namei,
            'id': get_resource_id(namei,data['imagen']['images'])
        },
        'network':{
            'name': namen,
            'id': get_resource_id(namen,data['network'])
        },
        'keypair':{
            'name': namekey,
            'id': get_resource_key(namekey,data['keypair'])
        },
        'flavor':{
            'name': namefla,
            'id': get_resource_id(namefla,data['flavor'])
        },
        'security_group':{
            'name': namesecu,
            'id': get_resource_id(namesecu,data['security_group'])
        }
    }