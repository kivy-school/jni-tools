from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.ByteBuffer import ByteBuffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES32:
    GL_BUFFER: ClassVar[int]
    GL_CLAMP_TO_BORDER: ClassVar[int]
    GL_COLORBURN: ClassVar[int]
    GL_COLORDODGE: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x10: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x6: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x8: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x10: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x12: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_4x4: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x4: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x6: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x6: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x8: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8: ClassVar[int]
    GL_CONTEXT_FLAGS: ClassVar[int]
    GL_CONTEXT_FLAG_DEBUG_BIT: ClassVar[int]
    GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT: ClassVar[int]
    GL_CONTEXT_LOST: ClassVar[int]
    GL_DARKEN: ClassVar[int]
    GL_DEBUG_CALLBACK_FUNCTION: ClassVar[int]
    GL_DEBUG_CALLBACK_USER_PARAM: ClassVar[int]
    GL_DEBUG_GROUP_STACK_DEPTH: ClassVar[int]
    GL_DEBUG_LOGGED_MESSAGES: ClassVar[int]
    GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH: ClassVar[int]
    GL_DEBUG_OUTPUT: ClassVar[int]
    GL_DEBUG_OUTPUT_SYNCHRONOUS: ClassVar[int]
    GL_DEBUG_SEVERITY_HIGH: ClassVar[int]
    GL_DEBUG_SEVERITY_LOW: ClassVar[int]
    GL_DEBUG_SEVERITY_MEDIUM: ClassVar[int]
    GL_DEBUG_SEVERITY_NOTIFICATION: ClassVar[int]
    GL_DEBUG_SOURCE_API: ClassVar[int]
    GL_DEBUG_SOURCE_APPLICATION: ClassVar[int]
    GL_DEBUG_SOURCE_OTHER: ClassVar[int]
    GL_DEBUG_SOURCE_SHADER_COMPILER: ClassVar[int]
    GL_DEBUG_SOURCE_THIRD_PARTY: ClassVar[int]
    GL_DEBUG_SOURCE_WINDOW_SYSTEM: ClassVar[int]
    GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR: ClassVar[int]
    GL_DEBUG_TYPE_ERROR: ClassVar[int]
    GL_DEBUG_TYPE_MARKER: ClassVar[int]
    GL_DEBUG_TYPE_OTHER: ClassVar[int]
    GL_DEBUG_TYPE_PERFORMANCE: ClassVar[int]
    GL_DEBUG_TYPE_POP_GROUP: ClassVar[int]
    GL_DEBUG_TYPE_PORTABILITY: ClassVar[int]
    GL_DEBUG_TYPE_PUSH_GROUP: ClassVar[int]
    GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR: ClassVar[int]
    GL_DIFFERENCE: ClassVar[int]
    GL_EXCLUSION: ClassVar[int]
    GL_FIRST_VERTEX_CONVENTION: ClassVar[int]
    GL_FRACTIONAL_EVEN: ClassVar[int]
    GL_FRACTIONAL_ODD: ClassVar[int]
    GL_FRAGMENT_INTERPOLATION_OFFSET_BITS: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_LAYERED: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_LAYERS: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS: ClassVar[int]
    GL_GEOMETRY_INPUT_TYPE: ClassVar[int]
    GL_GEOMETRY_OUTPUT_TYPE: ClassVar[int]
    GL_GEOMETRY_SHADER: ClassVar[int]
    GL_GEOMETRY_SHADER_BIT: ClassVar[int]
    GL_GEOMETRY_SHADER_INVOCATIONS: ClassVar[int]
    GL_GEOMETRY_VERTICES_OUT: ClassVar[int]
    GL_GUILTY_CONTEXT_RESET: ClassVar[int]
    GL_HARDLIGHT: ClassVar[int]
    GL_HSL_COLOR: ClassVar[int]
    GL_HSL_HUE: ClassVar[int]
    GL_HSL_LUMINOSITY: ClassVar[int]
    GL_HSL_SATURATION: ClassVar[int]
    GL_IMAGE_BUFFER: ClassVar[int]
    GL_IMAGE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_INNOCENT_CONTEXT_RESET: ClassVar[int]
    GL_INT_IMAGE_BUFFER: ClassVar[int]
    GL_INT_IMAGE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_BUFFER: ClassVar[int]
    GL_INT_SAMPLER_CUBE_MAP_ARRAY: ClassVar[int]
    GL_ISOLINES: ClassVar[int]
    GL_IS_PER_PATCH: ClassVar[int]
    GL_LAST_VERTEX_CONVENTION: ClassVar[int]
    GL_LAYER_PROVOKING_VERTEX: ClassVar[int]
    GL_LIGHTEN: ClassVar[int]
    GL_LINES_ADJACENCY: ClassVar[int]
    GL_LINE_STRIP_ADJACENCY: ClassVar[int]
    GL_LOSE_CONTEXT_ON_RESET: ClassVar[int]
    GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_DEBUG_GROUP_STACK_DEPTH: ClassVar[int]
    GL_MAX_DEBUG_LOGGED_MESSAGES: ClassVar[int]
    GL_MAX_DEBUG_MESSAGE_LENGTH: ClassVar[int]
    GL_MAX_FRAGMENT_INTERPOLATION_OFFSET: ClassVar[int]
    GL_MAX_FRAMEBUFFER_LAYERS: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_GEOMETRY_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_GEOMETRY_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_VERTICES: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_INVOCATIONS: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_LABEL_LENGTH: ClassVar[int]
    GL_MAX_PATCH_VERTICES: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_TESS_CONTROL_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_GEN_LEVEL: ClassVar[int]
    GL_MAX_TESS_PATCH_COMPONENTS: ClassVar[int]
    GL_MAX_TEXTURE_BUFFER_SIZE: ClassVar[int]
    GL_MIN_FRAGMENT_INTERPOLATION_OFFSET: ClassVar[int]
    GL_MIN_SAMPLE_SHADING_VALUE: ClassVar[int]
    GL_MULTIPLY: ClassVar[int]
    GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY: ClassVar[int]
    GL_MULTISAMPLE_LINE_WIDTH_RANGE: ClassVar[int]
    GL_NO_RESET_NOTIFICATION: ClassVar[int]
    GL_OVERLAY: ClassVar[int]
    GL_PATCHES: ClassVar[int]
    GL_PATCH_VERTICES: ClassVar[int]
    GL_PRIMITIVES_GENERATED: ClassVar[int]
    GL_PRIMITIVE_BOUNDING_BOX: ClassVar[int]
    GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED: ClassVar[int]
    GL_PROGRAM: ClassVar[int]
    GL_PROGRAM_PIPELINE: ClassVar[int]
    GL_QUADS: ClassVar[int]
    GL_QUERY: ClassVar[int]
    GL_REFERENCED_BY_GEOMETRY_SHADER: ClassVar[int]
    GL_REFERENCED_BY_TESS_CONTROL_SHADER: ClassVar[int]
    GL_REFERENCED_BY_TESS_EVALUATION_SHADER: ClassVar[int]
    GL_RESET_NOTIFICATION_STRATEGY: ClassVar[int]
    GL_SAMPLER: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_SAMPLER_BUFFER: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW: ClassVar[int]
    GL_SAMPLE_SHADING: ClassVar[int]
    GL_SCREEN: ClassVar[int]
    GL_SHADER: ClassVar[int]
    GL_SOFTLIGHT: ClassVar[int]
    GL_STACK_OVERFLOW: ClassVar[int]
    GL_STACK_UNDERFLOW: ClassVar[int]
    GL_TESS_CONTROL_OUTPUT_VERTICES: ClassVar[int]
    GL_TESS_CONTROL_SHADER: ClassVar[int]
    GL_TESS_CONTROL_SHADER_BIT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_BIT: ClassVar[int]
    GL_TESS_GEN_MODE: ClassVar[int]
    GL_TESS_GEN_POINT_MODE: ClassVar[int]
    GL_TESS_GEN_SPACING: ClassVar[int]
    GL_TESS_GEN_VERTEX_ORDER: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_BUFFER: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_ARRAY: ClassVar[int]
    GL_TEXTURE_BORDER_COLOR: ClassVar[int]
    GL_TEXTURE_BUFFER: ClassVar[int]
    GL_TEXTURE_BUFFER_BINDING: ClassVar[int]
    GL_TEXTURE_BUFFER_DATA_STORE_BINDING: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_TEXTURE_BUFFER_SIZE: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_TRIANGLES_ADJACENCY: ClassVar[int]
    GL_TRIANGLE_STRIP_ADJACENCY: ClassVar[int]
    GL_UNDEFINED_VERTEX: ClassVar[int]
    GL_UNKNOWN_CONTEXT_RESET: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_BUFFER: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_BUFFER: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY: ClassVar[int]
    GL_VERTEX_ARRAY: ClassVar[int]
    @staticmethod
    def glBlendBarrier() -> None: ...
    @staticmethod
    def glCopyImageSubData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControl(arg0: int, arg1: int, arg2: int, arg3: int, arg4: list[int], arg5: int, arg6: bool) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControl(arg0: int, arg1: int, arg2: int, arg3: int, arg4: IntBuffer, arg5: bool) -> None: ...
    @staticmethod
    def glDebugMessageInsert(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: str) -> None: ...
    @staticmethod
    def glDebugMessageCallback(arg0: "DebugProc") -> None: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(arg0: int, arg1: int, arg2: list[int], arg3: int, arg4: list[int], arg5: int, arg6: list[int], arg7: int, arg8: list[int], arg9: int, arg10: list[int], arg11: int, arg12: list[int], arg13: int) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(arg0: int, arg1: IntBuffer, arg2: IntBuffer, arg3: IntBuffer, arg4: IntBuffer, arg5: IntBuffer, arg6: ByteBuffer) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(arg0: int, arg1: list[int], arg2: int, arg3: list[int], arg4: int, arg5: list[int], arg6: int, arg7: list[int], arg8: int) -> list[str]: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(arg0: int, arg1: IntBuffer, arg2: IntBuffer, arg3: IntBuffer, arg4: IntBuffer) -> list[str]: ...
    @staticmethod
    def glPushDebugGroup(arg0: int, arg1: int, arg2: int, arg3: str) -> None: ...
    @staticmethod
    def glPopDebugGroup() -> None: ...
    @staticmethod
    def glObjectLabel(arg0: int, arg1: int, arg2: int, arg3: str) -> None: ...
    @staticmethod
    def glGetObjectLabel(arg0: int, arg1: int) -> str: ...
    @staticmethod
    def glObjectPtrLabel(arg0: int, arg1: str) -> None: ...
    @staticmethod
    def glGetObjectPtrLabel(arg0: int) -> str: ...
    @staticmethod
    def glGetPointerv(arg0: int) -> int: ...
    @staticmethod
    def glEnablei(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glDisablei(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBlendEquationi(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBlendEquationSeparatei(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glBlendFunci(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparatei(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glColorMaski(arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool) -> None: ...
    @staticmethod
    def glIsEnabledi(arg0: int, arg1: int) -> bool: ...
    @staticmethod
    def glDrawElementsBaseVertex(arg0: int, arg1: int, arg2: int, arg3: Buffer, arg4: int) -> None: ...
    @staticmethod
    def glDrawRangeElementsBaseVertex(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: Buffer, arg6: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstancedBaseVertex(arg0: int, arg1: int, arg2: int, arg3: Buffer, arg4: int, arg5: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstancedBaseVertex(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @staticmethod
    def glFramebufferTexture(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glPrimitiveBoundingBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> None: ...
    @staticmethod
    def glGetGraphicsResetStatus() -> int: ...
    @staticmethod
    def glReadnPixels(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformfv(arg0: int, arg1: int, arg2: int, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformfv(arg0: int, arg1: int, arg2: int, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformuiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformuiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @staticmethod
    def glMinSampleShading(arg0: float) -> None: ...
    @staticmethod
    def glPatchParameteri(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glTexBuffer(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glTexBufferRange(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glTexStorage3DMultisample(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool) -> None: ...

    class DebugProc:
        def onMessage(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str) -> None: ...
