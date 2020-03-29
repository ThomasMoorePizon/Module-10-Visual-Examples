# Module-10-Visual-Examples
4 Plot Examples
Changed from my work computer to personal computer - access to system path issues for pip
Created 2 plots in matplotlib that worked ok when I moved to the personal computer

ggplot is giving an error:
Traceback (most recent call last):
  File "plot2gg.py", line 2, in <module>
    from ggplot import ggplot
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\__init__.py", line 19, in <module>
    from .geoms import geom_area, geom_blank, geom_boxplot, geom_line, geom_point, geom_jitter, geom_histogram, geom_density, geom_hline, geom_vline, geom_bar, geom_abline, geom_tile, geom_rect, geom_bin2d, geom_step, geom_text, geom_path, geom_ribbon, geom_now_its_art, geom_violin, geom_errorbar, geom_polygon
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\geoms\__init__.py", line 1, in <module>
    from .geom_abline import geom_abline
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\geoms\geom_abline.py", line 1, in <module>
    from .geom import geom
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\geoms\geom.py", line 3, in <module>
    from ..ggplot import ggplot
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\ggplot.py", line 13, in <module>
    from .aes import aes
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\aes.py", line 11, in <module>
    from . import utils
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\utils.py", line 81, in <module>
    pd.tslib.Timestamp,
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\__init__.py", line 263, in __getattr__
    raise AttributeError(f"module 'pandas' has no attribute '{name}'")
AttributeError: module 'pandas' has no attribute 'tslib'
  
  Still working on it - 
  Traceback (most recent call last):
  File "plot2gg.py", line 2, in <module>
    from ggplot import *
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\__init__.py", line 19, in <module>
    from .geoms import geom_area, geom_blank, geom_boxplot, geom_line, geom_point, geom_jitter, geom_histogram, geom_density, geom_hline, geom_vline, geom_bar, geom_abline, geom_tile, geom_rect, geom_bin2d, geom_step, geom_text, geom_path, geom_ribbon, geom_now_its_art, geom_violin, geom_errorbar, geom_polygon
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\geoms\__init__.py", line 1, in <module>
    from .geom_abline import geom_abline
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\geoms\geom_abline.py", line 1, in <module>
    from .geom import geom
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\geoms\geom.py", line 3, in <module>
    from ..ggplot import ggplot
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\ggplot.py", line 13, in <module>
    from .aes import aes
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\aes.py", line 11, in <module>
    from . import utils
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\ggplot\utils.py", line 81, in <module>
    pd.tslib.Timestamp,
  File "C:\Users\shado\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\__init__.py", line 263, in __getattr__
    raise AttributeError(f"module 'pandas' has no attribute '{name}'")
AttributeError: module 'pandas' has no attribute 'tslib'
