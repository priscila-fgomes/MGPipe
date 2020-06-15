.. _documenting:
===============================
Known issues for OS X users
===============================

Problem with libcrypto.1.0.0.dylib when using Samtools
--------------------------------

.. code-block:: bash

    dyld: Library not loaded: @rpath/libcrypto.1.0.0.dylib
    Reason: image not found


Temporary fix:
--------------------------------
.. code-block:: bash

  # Uninstall and downgrade openssl to version 1.0.2
  brew uninstall --ignore-dependencies openssl
  brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/30fd2b68feb458656c2da2b91e577960b11c42f4/Formula/openssl.rb
 
