from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyChangeSupport"]

class PropertyChangeSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeSupport"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    addPropertyChangeListener = JavaMultipleMethod([("(Ljava/beans/PropertyChangeListener;)V", False, False), ("(Ljava/lang/String;Ljava/beans/PropertyChangeListener;)V", False, False)])
    removePropertyChangeListener = JavaMultipleMethod([("(Ljava/beans/PropertyChangeListener;)V", False, False), ("(Ljava/lang/String;Ljava/beans/PropertyChangeListener;)V", False, False)])
    firePropertyChange = JavaMultipleMethod([("(Ljava/beans/PropertyChangeEvent;)V", False, False), ("(Ljava/lang/String;ZZ)V", False, False), ("(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V", False, False), ("(Ljava/lang/String;II)V", False, False)])
    fireIndexedPropertyChange = JavaMultipleMethod([("(Ljava/lang/String;IZZ)V", False, False), ("(Ljava/lang/String;ILjava/lang/Object;Ljava/lang/Object;)V", False, False), ("(Ljava/lang/String;III)V", False, False)])
    hasListeners = JavaMethod("(Ljava/lang/String;)Z")
    getPropertyChangeListeners = JavaMultipleMethod([("()[Ljava/beans/PropertyChangeListener;", False, False), ("(Ljava/lang/String;)[Ljava/beans/PropertyChangeListener;", False, False)])