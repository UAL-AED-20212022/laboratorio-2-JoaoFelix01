from controllers.controller import *

def iniciar():
    
    try:
        
        while True:
            
            scan = input().split()
            match scan[0].upper():
                
                case "RPI":
                    rpi(scan, lista)
                
                case "RPF":
                    rpf(scan)
                
                case "RPDE":
                    rpde(scan)
                
                case "RPAE":
                    rpae(scan)
                
                case "RPII":
                    rpii(scan)
                
                case "VNE":
                    print (f"O número de elementos são {vne()}")
                
                case "VP":
                    if vp(scan) or not vp(scan) is None:
                        print (f"O país {scan[1]} não se encontra na lista.")
                    else:
                        print (f"O país {scan[1]} encontra-se na lista.")
                
                case "EPE":
                    x = epe()
                    print (f"O país {x} foi eliminado da lista")
                
                case "EUE":
                    x = eue()
                    print (f"O país {x} foi eliminado da lista")
                
                case "EP":
                    ep(scan)
                    if vp(scan) or not vp(scan) is None:
                        print (f"O país {scan[1]} não se encontra na lista.")
                    else:
                        print (f"O país {scan[1]} foi eliminado da lista")
                
                case _:
                    pass
    except:
        pass                  