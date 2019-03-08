import java.util.Scanner; 

public class PrintingCosts{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){
            int x = 0; 
            String s = sc.nextLine(); 
            for (int i = 0; i < s.length(); i++){
                char tmp = s.charAt(i); 
                switch (tmp){
                    //0-15
                    case 32:
                        x+=0; 
                        break;
                    case 39:
                    case 96:
                        x+=3; 
                        break;
                    case 46:
                        x+=4; 
                        break;
                    case 34:
                        x+=6; 
                        break;
                    case 44:
                    case 45:
                    case 94:
                        x+=7; 
                        break;
                    case 58:
                    case 95:
                        x+=8;
                        break;
                    case 33:
                    case 126:
                        x+=9;
                        break;
                    case 47:
                    case 60:
                    case 62:
                    case 92:
                        x+=10;
                        break;
                    case 59:
                        x+=11;
                        break;
                    case 40:
                    case 41:
                    case 124:
                        x+=12; 
                        break;
                    case 43:
                    case 118:
                    case 120:
                    case 114:
                        x+=13;
                        break;
                    case 89:
                    case 61:
                        x+=14;
                        break;
                    case 63:
                    case 105:
                        x+=15;
                        break;
                    //16-29
                    case 76:
                    case 108:
                    case 55:
                    case 84:
                        x+=16;
                        break;
                    case 42:
                    case 116:
                    case 99:
                    case 117:
                        x+=17;
                        break;
                    case 74:
                    case 110:
                    case 123:
                    case 93:
                    case 88:
                    case 125:
                    case 102:
                    case 73:
                    case 91:
                        x+=18;
                        break; 
                    case 122:
                    case 86:
                    case 119:
                    case 49:
                        x+=19;
                        break;
                    case 111:
                    case 70:
                    case 106:
                    case 67:
                        x+=20;
                        break;
                    case 104:
                    case 75:
                    case 52:
                    case 107:
                    case 115:
                        x+=21;
                        break;
                    case 37:
                    case 50:
                    case 48:
                    case 90:
                    case 109:
                        x+=22;
                        break;
                    case 51:
                    case 56:
                    case 80:
                    case 101:
                    case 85:
                    case 97:
                        x+=23;
                        break;
                    case 35:
                    case 38:
                    case 65:
                    case 121:
                        x+=24;
                        break;
                    case 98:
                    case 100:
                    case 112:
                    case 113:
                    case 83:
                    case 71:
                    case 72:
                    case 78:
                        x+=25;
                        break;
                    case 68:
                    case 57:
                    case 69:
                    case 54:
                    case 79:
                    case 87:
                        x+=26;
                        break;
                    case 53:
                        x+=27;
                        break;
                    case 82:
                    case 77:
                        x+=28;
                        break;
                    case 66:
                    case 36:
                        x+=29;
                        break;
                    // 30-32
                    case 103:
                        x+=30;
                        break;
                    case 81:
                        x+=31;
                        break;
                    case 64:
                        x+=32;
                        break;
                }
            }
            System.out.println(x); 
        }
    }
}