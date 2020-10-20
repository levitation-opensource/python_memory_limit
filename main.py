# -*- coding: utf-8 -*-




if __name__ == "__main__":  # subprocesses are automatically included in the aggregated accounting of the limits set to the main process

  if (1 == 1):   # prevent system hangs
  
    try:

      import os

      if os.name == 'nt':

        from windows_jobobject import set_mem_commit_limit

        mem_limit = 4 * 1024 * 1024 * 1024
        min_free_swap = 8 * 1024 * 1024 * 1024

        set_mem_commit_limit(os.getpid(), mem_limit, min_free_swap)

      else:   #/ if os.name == 'nt':

        from linux_rlimit import set_mem_limits

        data_size_limit = 512 * 1024 * 1024
        address_space_size_limit = 1024 * 1024 * 1024

        set_mem_limits(data_size_limit, address_space_size_limit)

      #/ if os.name == 'nt':

    except Exception as msg:
      print(msg)
      pass

  #/ if (1 == 1):

#/ if __name__ == "__main__":





# unleash your dragons here

print("hello")




