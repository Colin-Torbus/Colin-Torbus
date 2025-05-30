# format as dict[category[type[model]]]
new_dict = {
    'devices' : {
        'projector': {
            'p60' : {
                'manufacturer' : 'norxe',
                'country of origin' : 'norway',
                'description' : 'cool rectangle',
                'price' : '2.71'
            },
            'p10' : {
                'manufacturer' : 'norxe',
                'country of origin' : 'norway',
                'description' : 'not as cool rectangle',
                'price' : '5.86'
            },
        },
        'monitor' : {
            'lg50' : {
                'manufacturer' : 'lg',
                'country of origin' : 'zimbabwe',
                'description' : 'crt tv',
                'price' : '4.29'
            },
            'samsung69' : {
                'manufacturer' : 'samsung',
                'country of origin' : 'constantinople',
                'description' : '69 in tv',
                'price' : '69.69'
            },
        },
    },
    'cables & adapters' : {
        'active' : {
            'P-DPA30-50' : {
                'manufacturer' : 'Covid',
                'country of origin' : 'probably china',
                'description' : 'ACTIVE OPTICAL DISPLAYPORT CABLE, 8K, HBR3, DP 1.4, Ultra HD, with Locking Connectors, 50 ft, Plenum Rated',
                'price' : '$290.40'
            },
        },
        'passive' : {
            'NYC-604' : {
                'manufacturer' : 'New York Cables',
                'country of origin' : 'probably china',
                'description' : 'Green 1000ft Cat6 Plenum CCA Cable UTP CMP Rated 23 AWG 550 MHz Pull Box.',
                'price' : '$134.99'
            },
        },
    },
    'hardware' : {
        'mounting' : {
            'CC-106R' : {
                'manufacturer' : 'impact',
                'country of origin' : 'probably china',
                'description' : 'Super clamp for articulating camera mount.',
                'price' : '$29.95'
            },
            'BHE-107' : {
                'manufacturer' : 'impact',
                'country of origin' : 'probably china',
                'description' : '2 section articulating camera mount.',
                'price' : '$36.95'
            }  ,      
        },
    },
    'software' : {
        'scalable' : {
            'Scalable Display 11.0' : {
                'manufacturer' : 'Scalable Display Technologies',
                'country of origin' : 'United States',
                'description' : 'Software application for blending/warping geometry. Supports automatic camera based calibration system.',
                'price' : '$2650'
            },
        },
    },
    'installation, programming, engineering services' : {
        'labor' : {
            'Installation Supervisor' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'Site POC and team lead for installation. Oversees installation, configuration, alignment, testing, and training.',
                'price' : '$145',
            },
            'Installation Labor' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'On site technician for installation and configuration of equipment.',
                'price' : '$135',
            },
            'Configuration/Programming' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'EPDS technician to oversee configuration and programming of materials installed on site.',
                'price' : '$160',
            },
            'Scalable Technician' : {
                'manufacturer' : 'SDT',
                'country of origin' : None,
                'description' : 'Integrate Scalable Display into IGs and blend/warp projection system.',
                'price' : '$2250',
            },
        },
    },
    'testing' : {
        'labor' : {
            'Testing' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'Acceptance testing of visual system based on customer satisfaction/feedback. To be completed during EPDS and SDT time on site.',
                'price' : '$0',
            },
        },  
    },
    'training' : {
        'labor' : {
            'Training' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : '## FIXME ## CUSTOM',
                'price' : '$0',
            },
        },
    },
    'other expenses' : {
        'shop' : {
            'Shop Supplies' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'Misc. fasteners, connectors, cable ties, adapters, etc. for installation.',
                'price' : '## FIXME ## CUSTOM',
            },
            'Equipment rental' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : '## FIXME ## CUSTOM'
            },
        },
    },
    'travel' : {
        'transport' : {
            'Rental Car' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'Rental car for transporting EPDS/SDT personnel to and from site.',
                'price' : '## FIXME ## CUSTOM',
            },
            'Airfare' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'Round trip airfare including baggage costs. ## FIXME CUSTOM ##',
                'price' : '## FIXME ## CUSTOM',
            }
        },
        'living' : {
            'Lodging' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'Lodging for EPDS/STD personnel.',
                'price' : '## FIXME ## CUSTOM', 
            },
            'Travel Per Diem' : {
                'manufacturer' : 'EPDS',
                'country of origin' : None,
                'description' : 'Based on US GSA Per Diem Rates. Travel rates apply for EPDS/SDT staff on travel days (travel rate = standard rate x.75) ## FIXME CUSTOM ##',
                'price' : '## FIXME ## CUSTOM', 
            },
        },
    },
}