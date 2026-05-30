from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Channel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Channel"
    getSelectResponse = JavaMethod("()[B")
    getSession = JavaMethod("()Landroid/se/omapi/Session;")
    isBasicChannel = JavaMethod("()Z")
    selectNext = JavaMethod("()Z")
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")
    transmit = JavaMethod("([B)[B")

class Reader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Reader"
    closeSessions = JavaMethod("()V")
    getSEService = JavaMethod("()Landroid/se/omapi/SEService;")
    isSecureElementPresent = JavaMethod("()Z")
    getName = JavaMethod("()Ljava/lang/String;")
    openSession = JavaMethod("()Landroid/se/omapi/Session;")

class Session(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Session"
    closeChannels = JavaMethod("()V")
    getATR = JavaMethod("()[B")
    getReader = JavaMethod("()Landroid/se/omapi/Reader;")
    openBasicChannel = JavaMultipleMethod([("([BB)Landroid/se/omapi/Channel;", False, False), ("([B)Landroid/se/omapi/Channel;", False, False)])
    openLogicalChannel = JavaMultipleMethod([("([B)Landroid/se/omapi/Channel;", False, False), ("([BB)Landroid/se/omapi/Channel;", False, False)])
    close = JavaMethod("()V")
    isClosed = JavaMethod("()Z")

class SEService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/SEService"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/util/concurrent/Executor;Landroid/se/omapi/SEService$OnConnectedListener;)V", False)]
    ACTION_SECURE_ELEMENT_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    EXTRA_READER_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_READER_STATE = JavaStaticField("Ljava/lang/String;")
    isConnected = JavaMethod("()Z")
    getReaders = JavaMethod("()[Landroid/se/omapi/Reader;")
    getUiccReader = JavaMethod("(I)Landroid/se/omapi/Reader;")
    getVersion = JavaMethod("()Ljava/lang/String;")
    shutdown = JavaMethod("()V")

    class OnConnectedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/se/omapi/SEService$OnConnectedListener"
        onConnected = JavaMethod("()V")