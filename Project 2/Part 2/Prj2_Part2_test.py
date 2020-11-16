import unittest
import random
from Project_2 import *

US_AREA = ['205','251','256','334','659','938','907','236','250','778','480','520','602','623','928','327','479','501','870','209','213','279','310','323','341',
'408','415','424','442','510','530','559','562','619','626','628','650','657','661','669','707','714','747','760','805','818','820','831','840','858',
'909','916','925','949','951','303','719','720','970','203','475','860','959','302','202','239','305','321','352','386','407','448','561','689','727',
'754','772','786','813','850','863','904','941','954','229','404','470','478','678','706','762','770','912','808','208','986','217','224','309','312',
'331','447','464','618','630','708','730','773','779','815','847','872','219','260','317','463','574','765','812','930','319','515','563','641','712',
'316','620','785','913','270','364','502','606','859','225','318','337','504','985','207','227','240','301','410','443','667','339','351','413','508',
'617','774','781','857','978','231','248','269','313','517','586','616','734','810','906','947','989','218','320','507','612','651','763','952','228',
'601','662','769','314','417','573','636','660','816','406','308','402','531','702','725','775','603','201','551','609','640','732','848','856','862',
'908','973','505','575','212','315','332','347','516','518','585','607','631','646','680','716','718','838','845','914','917','929','934','252','336',
'704','743','828','910','919','980','984','701','216','220','234','326','330','380','419','440','513','567','614','740','937','405','539','572','580',
'918','458','503','541','971','215','223','267','272','412','445','484','570','610','717','724','814','878','401','803','839','843','854','864','605',
'423','615','629','731','865','901','931','210','214','254','281','325','346','361','409','430','432','469','512','682','713','726','737','806','817',
'830','832','903','915','936','940','945','956','972','979','385','435','801','802','276','434','540','571','703','757','804','948','206','253','360',
'425','509','564','304','681','262','274','414','534','608','715','920','307']
    
class Functions_Tester(unittest.TestCase):

  def test_make_prefix(self):
    print('\n\nTest make_prefix base')
    try:
      prefix = make_prefix()
      print('Return value was', prefix)
      print('Checking type')
      self.assertEqual(type(prefix), str)
      print('Checking length')
      self.assertEqual(len(prefix), 3)
      print('Checking for composition')
      self.assertTrue(prefix.isdigit())
      print('Checking validity')
      self.assertTrue(prefix not in ['555', '958', '959'] and prefix[1:] != '11')
    except BaseException as e:
      print(e)
      print('Testing failed.')

  def test_make_suffix(self):
    print('\n\nTest make_suffix base')
    try:
      suffix = make_suffix()
      print('Return value was', suffix)
      print('Checking type')
      self.assertEqual(type(suffix), str)
      print('Checking length')
      self.assertEqual(len(suffix), 4)
      print('Checking composition')
      self.assertTrue(suffix.isdigit())
    except BaseException as e:
      print(e)
      print('Testing failed.')


  def test_make_phone_number_default(self):
    print('\n\nTest make_phone_number default case')
    try:
      result = make_phone_number()
      print('Return value was', result)
      print('Checking correct format of number:')
      print('Checking type:')
      self.assertEqual(type(result), str)
      print('Checking length:')
      self.assertEqual(len(result), 12)
      print('Checking correct separator and placement:')
      data = result.split('-')
      self.assertEqual(len(data[0]), 3)
      self.assertEqual(len(data[1]), 3)
      self.assertEqual(len(data[2]), 4)
      self.assertTrue(result.replace('-','').isnumeric())
      print('Checking valid area')
      self.assertTrue(data[0] in US_AREA)
    except BaseException as e:
      print(e)
      print('Testing failed.')
      
  def test_make_phone_number_sep(self):
    print('\n\nTest make_phone_number sep #')
    try:
      result = make_phone_number(sep = '#')
      print('Return value was', result)
      print('Checking correct format of number:')
      print('Checking type:')
      self.assertEqual(type(result), str)
      print('Checking length:')
      self.assertEqual(len(result), 12)
      print('Checking correct separator and placement:')
      data = result.split('#')
      self.assertEqual(len(data[0]), 3)
      self.assertEqual(len(data[1]), 3)
      self.assertEqual(len(data[2]), 4)
      self.assertTrue(result.replace('#','').isnumeric())
      print('Checking valid area')
      self.assertTrue(data[0] in US_AREA)
    except BaseException as e:
      print(e)
      print('Testing failed.')
      
  def test_make_phone_number_custom(self):
    print('\n\nTest make_phone_number custom')
    try:
      result = make_phone_number(['757', '858'])
      print('Return value was', result)
      print('Checking correct format of number:')
      print('Checking type:')
      self.assertEqual(type(result), str)
      print('Checking length:')
      self.assertEqual(len(result), 12)
      print('Checking correct separator and placement:')
      data = result.split('-')
      self.assertEqual(len(data[0]), 3)
      self.assertEqual(len(data[1]), 3)
      self.assertEqual(len(data[2]), 4)
      self.assertTrue(result.replace('-','').isnumeric())
      print('Checking valid area')
      self.assertTrue(data[0] in ['757', '858'])
    except BaseException as e:
      print(e)
      print('Testing failed.')



if __name__ == '__main__':
  unittest.main()
  