Usage
=====

.. _installation:

Installation
------------

To use slskd-api, first install it using pip:

.. code-block:: console

   (.venv) $ pip install slskd-api

Send requests to the server
---------------------------

Once the module is installed, you can create an instance of slskd client with the following code, 
granted an API-Key was setup in your `slskd configuration file <https://github.com/slskd/slskd/blob/master/docs/config.md#yaml-18>`_.

.. code-block:: console

   import slskd_api
   slskd = slskd_api.SlskdClient(host, api_key, url_base)

From there all APIs (with the exception of :py:class:`~slskd_api.MetricsApi`) 
will be accessible through ``slskd``:

.. code-block:: console

   app_status = slskd.application.state()
   available_rooms = slskd.rooms.get_all()

