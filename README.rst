DEPRECATED: this functionality now covered by Sesam DTL

====================
sesam-base64-converter
====================



Microservice for converting anything to base64 and return back

.. image:: https://travis-ci.org/timurgen/sesam-base64-converter.svg?branch=master
    :target: https://travis-ci.org/timurgen/sesam-base64-converter

example configuration 
::
    system config
    {
      "_id": "testbase64",
      "type": "system:microservice",
      "docker": {
        "environment": {
            "PAYLOAD_PROPERTY": "entities"
        },
        "image": "ohuenno/base64sesam",
        "port": 5000
      }
    }
    pipe transform config
    {
        "type": "http",
        "system": "testbase64",
        "url": "/"
      }
