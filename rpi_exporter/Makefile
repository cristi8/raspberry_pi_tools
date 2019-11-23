

install:
	sudo pip3 install prometheus_client
	sudo cp rpi_exporter.py /usr/sbin/
	sudo cp rpi_exporter.service /lib/systemd/system/

	sudo chmod +x /usr/sbin/rpi_exporter.py
	sudo systemctl enable rpi_exporter
	sudo systemctl start rpi_exporter


uninstall:
	sudo systemctl disable rpi_exporter
	sudo systemctl stop rpi_exporter
	sudo rm -f \
		/usr/sbin/rpi_exporter.py \
		/lib/systemd/system/rpi_exporter.service
