import json
import boto3
import sys, os

glue = boto3.client("glue")

def lambda_handler(event, context):
    
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_object = event['Records'][0]['s3']['object']['key']
    
    parse_id_source = s3_object.split('/')[2]
    if parse_id_source == 'cliente':
      glue.start_crawler(Name = 'RAW_CLIENTE_PERFIL')
    elif parse_id_source == 'productos':
      glue.start_crawler(Name = 'RAW_PRODUCTOS') 
    elif parse_id_source == 'prestamos':
      glue.start_crawler(Name = 'RAW_PRESTAMOS')
    elif parse_id_source == 'rentabilidad':
      glue.start_crawler(Name = 'RAW_RENTABILIDAD')
    elif parse_id_source == 'estadocivil':
      glue.start_crawler(Name = 'RAW_ESTADO_CIVIL')
    elif parse_id_source == 'segmento':
      glue.start_crawler(Name = 'RAW_SEGMENTO')
    elif parse_id_source == 'agencia':
      glue.start_crawler(Name = 'RAW_AGENCIA')
    elif parse_id_source == 'tipoprestamo':
      glue.start_crawler(Name = 'RAW_TIPO_PRESTAMO')
    elif parse_id_source == 'ubigeo':
      glue.start_crawler(Name = 'RAW_UBIGEO')

    return {
        'statusCode': 200,
        'body': json.dumps('Crawler en ejecución')
    }
