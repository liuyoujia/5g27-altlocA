import os, sys

def main(pdb_file_name,
         mtz_file_name,
         ligand_selection,
         ):
  pymol_selection = ligand_selection.replace('resname','resn')
  pymol_script = '''
  # set defaults
  set ray_opaque_background, off
  bg_color white
  # load model
  load %(pdb_file_name)s
  #''' % locals()

  # cmd = 'phenix.maps %(pdb_file_name)s %(mtz_file_name)s' % locals()
  # 4WWL_refine_2_2mFo-DFc_map.ccp4

  cmd = 'phenix.mtz2map %(mtz_file_name)s %(pdb_file_name)s' % locals()
  print cmd
  os.system(cmd)

  pymol_script += '''
  # load Polder map
  load %s_1.ccp4, polder
  isomesh polder_surface, polder, 2.5
  zoom %s
  show sticks, %s
  color grey, polder_surface
  ''' % (mtz_file_name.replace('.mtz',''),
         pymol_selection,
         pymol_selection,
         )

  print '\n\n\n\n'
  print pymol_script

  f=file('%s_%s.txt' % (pdb_file_name.replace('.pdb',''),
                        ligand_selection.replace(' ','_')
                        ), 'wb')
  f.write(pymol_script)
  del f

if __name__ == '__main__':
  main(*tuple(sys.argv[1:]))
