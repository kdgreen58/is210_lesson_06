    #!/usr/bin/env python -tt
    # -*- coding: utf-8 -*-
    """ task_03 bubble sort """
    import data

    def bubble_sort(blob):
        """ task_03 bubble """
        for index in range(len(blob)-1, 0, -1):
            for i in range(index):
                if blob[i] > blob[i+1]:
                    swap = blob[i]
                    blob[i] = blob[i+1]
                    blob[i+1] = swap
        return blob

    print bubble_sort(data.TASK_O1)
