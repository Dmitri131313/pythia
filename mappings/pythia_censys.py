pythia_censys_mappings={
  "and":"and",
  "or":"or",
  "not":"not",
  "*":"*",
  ":":":",
  "=":"=",
  "label":"labels",
  "ip_address":"ip",
  "cidr":"ip",
  "server":"name",
  "domain":"name",
  "hostname":"dns.names",
  "organization":"name",
  "port_number":"services.port",
  "base_protocol":"services.transport_protocol",
  "protocol":"services.service_name",
  "port_size_gt":"",
  "port_size_lt":"",
  "port_size":"service_count",
  "operating_system":"operating_system.product",
  "application":"services.software",
  "product_version":"services.software.version",
  "product":"services.software.product",
  "time_scanned":"last_updated_at",
  "common_platform_enumeration_cpe":"services.software.cpe",
  "country_code":"location.country_code",
  "country_name":"location.country",
  "postal_code":"location.postal_code",
  "state_name":"location.province",
  "region_name":"location.continent",
  "city_name":"location.city",
  "autonomous_system_number":"autonomous_system.asn",
  "autonomous_system_name":"autonomous_system.name",
  "autonomous_system_organization":"autonomous_system.organization",
  "http_title":"services.http.response.html_title",
  "http_header_hash":"services.banner_hashes",
  "http_header":"services.http.response.headers.value.headers",
  "service_banner_hash":"services.banner_hashes",
  "service_banner":"services.banner",
  "http_body_hash":"services.http.response.body_hashes",
  "http_body":"services.http.response.body",
  "http_status_code":"services.http.response.status_code",
  "http_favicon_hash_dec":"services.http.response.favicons.shodan_hash",
  "http_favicon_hash":"services.http.response.favicons.md5_hash",
  "tls_certificate_issuer_org":"services.tls.certificate.parsed.issuer.organization",
  "tls_certificate_subject_org":"services.tls.certificate.parsed.subject.organization",
  "tls_certificate_subject_cn":"services.tls.certificate.parsed.subject.common_name",
  "tls_certificate_issuer_cn":"services.tls.certificate.parsed.issuer.common_name",
  "tls_certificate_issuer":"services.tls.certificate.parsed.issuer",
  "tls_certificate_subject":"services.tls.certificate.parsed.subject",
  "tls_certificate_not_after":"services.tls.certificate.parsed.validity_period.not_after",
  "tls_certificate_not_before":"services.tls.certificate.parsed.validity_period.not_before",
  "tls_certificate_sha1":"services.tls.certificate.fingerprint_sha1",
  "tls_certificate_sha256":"services.tls.certificate.fingerprint_sha256",
  "tls_certificate_md5":"services.tls.certificate.fingerprint_md5",
  "tls_certificate_is_expired":"services.tls.certificate.revoked:true",
  "tls_certificate.is_valid":"services.tls.certificate.revoked:false",
  "tls_certificate.pubkey_rsa_bits":"services.tls.certificates.leaf_data.public_key.rsa.length",
  "tls_certificate_pubkey_ecdsa_bits":"services.ssh.server_host_key.ecdsa_public_key.length",
  "tls_certificate_pubkey_type":"services.tls.certificates.leaf_data.pubkey_algorithm",
  "tls_certificate_cipher_name":"services.tls.cipher_selected",
  "tls_certificate_algorithm":"services.tls.certificates.leaf_data.pubkey_algorithm",
  "tls_certificate_version":"services.tls.version_selected",
  "tls_certificate":"services.certificate",
  "jarm_fingerprint":"services.jarm.fingerprint",
  "ja3s_fingerprint":"services.tls.ja3s",
  "ja4s_fingerprint":"services.tls.ja4s",
  "ssh_hassh":"services.ssh.hassh_fingerprint",
  "ssh_banner_sha256":"services.banner_hashes",
  "ssh_banner":"services.banner",
  "ssh_key_length":"services.ssh.server_host_key.rsa_public_key.length",
  "ssh_fingerprint":"services.ssh.server_host_key.fingerprint_sha256"
}
