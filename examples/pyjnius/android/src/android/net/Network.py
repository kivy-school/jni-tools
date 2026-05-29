from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Network"]

class Network(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/Network"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSocketFactory = JavaMethod("()Ljavax/net/SocketFactory;")
    getAllByName = JavaMethod("(Ljava/lang/String;)[Ljava/net/InetAddress;")
    getNetworkHandle = JavaMethod("()J")
    bindSocket = JavaMultipleMethod([("(Ljava/net/DatagramSocket;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False), ("(Ljava/net/Socket;)V", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getByName = JavaMethod("(Ljava/lang/String;)Ljava/net/InetAddress;")
    openConnection = JavaMultipleMethod([("(Ljava/net/URL;Ljava/net/Proxy;)Ljava/net/URLConnection;", False, False), ("(Ljava/net/URL;)Ljava/net/URLConnection;", False, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    fromNetworkHandle = JavaStaticMethod("(J)Landroid/net/Network;")