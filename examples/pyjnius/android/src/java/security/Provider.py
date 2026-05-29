from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Provider"]

class Provider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Provider"
    getInfo = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    remove = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaMethod("()Ljava/util/Collection;")
    load = JavaMethod("(Ljava/io/InputStream;)V")
    clear = JavaMethod("()V")
    replace = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    merge = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    putIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    compute = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    computeIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/Function;)Ljava/lang/Object;")
    keySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    keys = JavaMethod("()Ljava/util/Enumeration;")
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    computeIfPresent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    getService = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/Provider$Service;")
    configure = JavaMethod("(Ljava/lang/String;)Ljava/security/Provider;")
    isConfigured = JavaMethod("()Z")
    getVersionStr = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()D")
    getServices = JavaMethod("()Ljava/util/Set;")

    class Service(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/Provider$Service"
        __javaconstructor__ = [("(Ljava/security/Provider;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/List;Ljava/util/Map;)V", False)]
        getProvider = JavaMethod("()Ljava/security/Provider;")
        supportsParameter = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        newInstance = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
        getType = JavaMethod("()Ljava/lang/String;")
        getClassName = JavaMethod("()Ljava/lang/String;")
        getAlgorithm = JavaMethod("()Ljava/lang/String;")
        getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")