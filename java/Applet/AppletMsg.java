package Applet;
import java.awt.*;
import java.applet.*;

public class AppletMsg extends Applet{
@Override
public void start() {
}
    @Override
    public void paint(Graphics g) {
        g.drawString("Hello World This is applet", 100,100);
    }
}
