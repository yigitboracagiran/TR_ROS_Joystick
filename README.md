A) Gereksinimler:

1- Bilgisayarınızda ROS Melodic veya ROS Noetic kurulu olmalıdır.

2- Turtlebot3 Gazebo’da çalıştırılabiliyor olmalıdır.

3- ROS ile uyumlu Joystick’e sahip olunmalıdır. Ör: Logitech F710 Kablosuz Gamepad

B) Joy Paketinin Kurulumu

1- Bilgisayara ROS’un Joy paketi “sudo apt-get install ros-<ros_sürümü>-joy” komutu ile kuruldu.

Not: ROS Sürümü kısmına sürümü küçük harflerle yazınız.

Ör: ros-melodic-joy

C) Joy Düğümünün Çalıştırılması

2- Joy düğümünü çalıştıracak launch dosyası yazıldı. Dosya ektedir.

Not: Joystick’in dev ve dev_ff değerlerini öğrenmek için terminale “ls -la /dev/input/by-id/”
komutunu yazınız.

Not: usb-.....-event-joystick ile biten değerin sonunda gelen değer (event18) dev_ff parametresi için;
usb-.....-joystick ile biten değerin sonunda gelen değer (js0) dev parametresi içindir.

3- Artık Joy paketi çalışıyor olmalıdır. Çalıştırmak için launch dosyasının olduğu dizine gidip
aşağıdaki komutu yazınız:

roslaunch <launch_dosyası>

4- Yeni bir terminal açıp “rostopic list” komutunu yazınız. /joy topic’i gözüküyor olmalıdır. Eğer
gözükmüyorsa yukarıdaki adımları tekrar gözden geçiriniz.

5- Terminale “rostopic echo /joy” komutunu yazıldığında; Joystick’te tuşlara basılırsa, ekranda
değişen değerlerden Joystick üzerinde bulunan tüm tuş ve joysticklerin yerlerini /Joy topic’inin
button ve axes dizilerinde bulabilir ve bir kod yazarak robotu Joystick ile kontrol edebilirsiniz.

Ör: Yeşil tuşa basıldığında button dizisinin 0. indeksindeki değer 1 olmaktadır.

D) Hız Kontrolü

1- Ekteki kodu çalıştırmadan önce:

a) Simülasyonda Turtlebot3 launch edilmelidir.

Ör: "roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch"

b) /joy topic’ini yayınlayan ekteki launch dosyası yukarıda anlatıldığı gibi çalıştırılmalıdır.

2- Son olarak terminalde kodun olduğu dizine gidilip "python joystick.py" komutu ile kod çalıştırılmalıdır. Kodun çalıştırılmasıyla Joystick ile simülasyonda Turtlebot3'ün hızı kontrol edilebiyor olunmalıdır.
