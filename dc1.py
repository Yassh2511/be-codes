import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ConcatInterface extends Remote {
    // The remote method signature
    String concatenate(String s1, String s2) throws RemoteException;
}

import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ConcatServer extends UnicastRemoteObject implements ConcatInterface {

    public ConcatServer() throws RemoteException {
        super();
    }

    @Override
    public String concatenate(String s1, String s2) throws RemoteException {
        System.out.println("Server received: '" + s1 + "' and '" + s2 + "'");
        return s1 + s2; // The actual computation
    }

    public static void main(String[] args) {
        try {
            ConcatServer obj = new ConcatServer();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("ConcatService", obj);
            System.out.println("Concatenation Server is ready...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
        }
    }
} server

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class ConcatClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            ConcatInterface stub = (ConcatInterface) registry.lookup("ConcatService");

            Scanner sc = new Scanner(System.in);
            System.out.print("Enter first string: ");
            String str1 = sc.next();
            System.out.print("Enter second string: ");
            String str2 = sc.next();

            // RPC call
            String result = stub.concatenate(str1, str2);

            System.out.println("Result from Server: " + result);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
        }
    }
}
