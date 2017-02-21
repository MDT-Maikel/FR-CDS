# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 11.0.1 for Linux x86 (64-bit) (September 21, 2016)
# Date: Tue 21 Feb 2017 10:41:19


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

P__tilde__DMS = Particle(pdg_code = 9000101,
                         name = '~DMS',
                         antiname = '~DMS',
                         spin = 1,
                         color = 1,
                         mass = Param.MDM,
                         width = Param.ZERO,
                         texname = '~DMS',
                         antitexname = '~DMS',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__DMC = Particle(pdg_code = 9000201,
                         name = '~DMC',
                         antiname = '~DMC~',
                         spin = 1,
                         color = 1,
                         mass = Param.MDM,
                         width = Param.ZERO,
                         texname = '~DMC',
                         antitexname = '~DMC~',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__DMC__tilde__ = P__tilde__DMC.anti()

P__tilde__DMM = Particle(pdg_code = 9000301,
                         name = '~DMM',
                         antiname = '~DMM',
                         spin = 2,
                         color = 1,
                         mass = Param.MDM,
                         width = Param.ZERO,
                         texname = '~DMM',
                         antitexname = '~DMM',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__DMF = Particle(pdg_code = 9000401,
                         name = '~DMF',
                         antiname = '~DMF~',
                         spin = 2,
                         color = 1,
                         mass = Param.MDM,
                         width = Param.ZERO,
                         texname = '~DMF',
                         antitexname = '~DMF~',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__DMF__tilde__ = P__tilde__DMF.anti()

P__tilde__DMV = Particle(pdg_code = 9000501,
                         name = '~DMV',
                         antiname = '~DMV',
                         spin = 3,
                         color = 1,
                         mass = Param.MDM,
                         width = Param.ZERO,
                         texname = '~DMV',
                         antitexname = '~DMV',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__DMW = Particle(pdg_code = 9000601,
                         name = '~DMW',
                         antiname = '~DMW~',
                         spin = 3,
                         color = 1,
                         mass = Param.MDM,
                         width = Param.ZERO,
                         texname = '~DMW',
                         antitexname = '~DMW~',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__DMW__tilde__ = P__tilde__DMW.anti()

P__tilde__XS8 = Particle(pdg_code = 9000108,
                         name = '~XS8',
                         antiname = '~XS8',
                         spin = 1,
                         color = 8,
                         mass = Param.MX,
                         width = Param.WXS8,
                         texname = '~XS8',
                         antitexname = '~XS8',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XC3 = Particle(pdg_code = 9000203,
                         name = '~XC3',
                         antiname = '~XC3~',
                         spin = 1,
                         color = 3,
                         mass = Param.MX,
                         width = Param.WXC3,
                         texname = '~XC3',
                         antitexname = '~XC3~',
                         charge = -1/3,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XC3__tilde__ = P__tilde__XC3.anti()

P__tilde__XC6 = Particle(pdg_code = 9000206,
                         name = '~XC6',
                         antiname = '~XC6~',
                         spin = 1,
                         color = 6,
                         mass = Param.MX,
                         width = Param.WXC6,
                         texname = '~XC6',
                         antitexname = '~XC6~',
                         charge = 4/3,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XC6__tilde__ = P__tilde__XC6.anti()

P__tilde__XC8 = Particle(pdg_code = 9000208,
                         name = '~XC8',
                         antiname = '~XC8~',
                         spin = 1,
                         color = 8,
                         mass = Param.MX,
                         width = Param.WXC8,
                         texname = '~XC8',
                         antitexname = '~XC8~',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XC8__tilde__ = P__tilde__XC8.anti()

P__tilde__XM8 = Particle(pdg_code = 9000308,
                         name = '~XM8',
                         antiname = '~XM8',
                         spin = 2,
                         color = 8,
                         mass = Param.MX,
                         width = Param.WXM8,
                         texname = '~XM8',
                         antitexname = '~XM8',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XF3 = Particle(pdg_code = 9000403,
                         name = '~XF3',
                         antiname = '~XF3~',
                         spin = 2,
                         color = 3,
                         mass = Param.MX,
                         width = Param.WXF3,
                         texname = '~XF3',
                         antitexname = '~XF3~',
                         charge = -1/3,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XF3__tilde__ = P__tilde__XF3.anti()

P__tilde__XF6 = Particle(pdg_code = 9000406,
                         name = '~XF6',
                         antiname = '~XF6~',
                         spin = 2,
                         color = 6,
                         mass = Param.MX,
                         width = Param.WXF6,
                         texname = '~XF6',
                         antitexname = '~XF6~',
                         charge = 4/3,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XF6__tilde__ = P__tilde__XF6.anti()

P__tilde__XF8 = Particle(pdg_code = 9000408,
                         name = '~XF8',
                         antiname = '~XF8~',
                         spin = 2,
                         color = 8,
                         mass = Param.MX,
                         width = Param.WXF8,
                         texname = '~XF8',
                         antitexname = '~XF8~',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XF8__tilde__ = P__tilde__XF8.anti()

P__tilde__XV8 = Particle(pdg_code = 9000508,
                         name = '~XV8',
                         antiname = '~XV8',
                         spin = 3,
                         color = 8,
                         mass = Param.MX,
                         width = Param.WXV8,
                         texname = '~XV8',
                         antitexname = '~XV8',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XW3 = Particle(pdg_code = 9000603,
                         name = '~XW3',
                         antiname = '~XW3~',
                         spin = 3,
                         color = 3,
                         mass = Param.MX,
                         width = Param.WXW3,
                         texname = '~XW3',
                         antitexname = '~XW3~',
                         charge = -1/3,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XW3__tilde__ = P__tilde__XW3.anti()

P__tilde__XW6 = Particle(pdg_code = 9000606,
                         name = '~XW6',
                         antiname = '~XW6~',
                         spin = 3,
                         color = 6,
                         mass = Param.MX,
                         width = Param.WXW6,
                         texname = '~XW6',
                         antitexname = '~XW6~',
                         charge = 4/3,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XW6__tilde__ = P__tilde__XW6.anti()

P__tilde__XW8 = Particle(pdg_code = 9000608,
                         name = '~XW8',
                         antiname = '~XW8~',
                         spin = 3,
                         color = 8,
                         mass = Param.MX,
                         width = Param.WXW8,
                         texname = '~XW8',
                         antitexname = '~XW8~',
                         charge = 0,
                         GhostNumber = 0,
                         LeptonNumber = 0,
                         Y = 0)

P__tilde__XW8__tilde__ = P__tilde__XW8.anti()

MC6 = Particle(pdg_code = 9002006,
               name = 'MC6',
               antiname = 'MC6~',
               spin = 1,
               color = 6,
               mass = Param.MMED,
               width = Param.WMC6,
               texname = 'MC6',
               antitexname = 'MC6~',
               charge = 4/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

MC6__tilde__ = MC6.anti()

