from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Network"]

class Network(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/Network"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAllByName = JavaMethod("(Ljava/lang/String;)[Ljava/net/InetAddress;")
    getByName = JavaMethod("(Ljava/lang/String;)Ljava/net/InetAddress;")
    getSocketFactory = JavaMethod("()Ljavax/net/SocketFactory;")
    openConnection = JavaMultipleMethod([("(Ljava/net/URL;)Ljava/net/URLConnection;", False, False), ("(Ljava/net/URL;Ljava/net/Proxy;)Ljava/net/URLConnection;", False, False)])
    bindSocket = JavaMultipleMethod([("(Ljava/net/DatagramSocket;)V", False, False), ("(Ljava/net/Socket;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False)])
    fromNetworkHandle = JavaStaticMethod("(J)Landroid/net/Network;")
    getNetworkHandle = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")