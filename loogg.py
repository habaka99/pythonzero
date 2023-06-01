#looginf
import logging
logging.basicConfig(filename="app1.log",filemode="a",
                    format=" (%(asctime)s)=> |%(name)s| %(levelname)s=> '%(message)s' ",datefmt="%d -%B -%Y -%H:%M:%S")
my_logger=logging.getLogger("abdo")
my_logger.critical("This Critical Message")