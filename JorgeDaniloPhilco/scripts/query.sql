select 
cliente.codigo,
agencia.zona,
prestamos.contrato,
prestamos.desembolso,
prestamos.saldo_real,
prestamos.monto_cuota,
prestamos.cuotas_pendientes,
cliente.ingreso,
cliente.uso_cajero,
cliente.uso_internet,
productos.cta_ahorro,
productos.saldo_ahorro,
productos.cta_cts,
productos.saldo_tarjeta,
prestamos.fecha_vencimiento,
cliente.fh_alta as fecha_alta
from cliente
left join agencia on cliente.cod_agencia = agencia.cod_agencia
left join prestamos on cliente.codigo = prestamos.codigo
left join productos on cliente.codigo = productos.codigo
