Weaviate
===========

Batch process all your records using ``unstructured-ingest`` to store structured outputs locally on your filesystem and upload those local files to a Weaviate collection.

First you'll need to install the weaviate dependencies as shown here.

.. code:: shell

  pip install "unstructured[weaviate]"

Run Locally
-----------
The upstream connector can be any of the ones supported, but for convenience here, showing a sample command using the
upstream local connector. This will push elements into a collection schema of your choice into a weaviate instance
running locally.

.. tabs::

   .. tab:: Shell

      .. literalinclude:: ./code/bash/weaviate.sh
         :language: bash

   .. tab:: Python

      .. literalinclude:: ./code/python/weaviate.py
         :language: python


For a full list of the options the CLI accepts check ``unstructured-ingest <upstream connector> weaviate --help``.

NOTE: Keep in mind that you will need to have all the appropriate extras and dependencies for the file types of the documents contained in your data storage platform if you're running this locally. You can find more information about this in the `installation guide <https://unstructured-io.github.io/unstructured/installing.html>`_.

Sample Index Schema
-------------------

To make sure the schema of the index matches the data being written to it, a sample schema json can be used:

.. literalinclude:: ./data/weaviate_elements_class.json
   :language: json
   :linenos:
   :caption: Object description