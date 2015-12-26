from luigi import s3
s3.S3Client().put("/Users/jpiper/pipeline.out.vcf", "s3://hli-bix-us-west-2/jpiper/pipeline.out.vcf", encrypt_key=True)

#s3.S3Client().copy("s3://hli-annotation/v2/exactest/parsed/ExAc/exac_liftover_normalized.json", "s3://hli-bix-us-west-2/jpiper/test.json", encrypt_key=True)

