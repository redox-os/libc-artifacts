*asm:
%{m32:--32} %{m64:--64} %{mx32:--x32}

*asm_debug:
%{!g0:%{gstabs*:--gstabs}%{!gstabs*:%{g*:--gdwarf2}}} %{fdebug-prefix-map=*:--debug-prefix-map %*}

*asm_final:
%{gsplit-dwarf:
       objcopy --extract-dwo 	 %{c:%{o*:%*}%{!o*:%b%O}}%{!c:%U%O} 	 %{c:%{o*:%:replace-extension(%{o*:%*} .dwo)}%{!o*:%b.dwo}}%{!c:%b.dwo}
       objcopy --strip-dwo 	 %{c:%{o*:%*}%{!o*:%b%O}}%{!c:%U%O}     }

*asm_options:
%{-target-help:%:print-asm-header()}  %{gz*:%e-gz is not supported in this configuration} %a %Y %{c:%W{o*}%{!o*:-o %w%b%O}}%{!c:-o %d%w%u%O}

*invoke_as:
%{!fwpa*:   %{fcompare-debug=*|fdump-final-insns=*:%:compare-debug-dump-opt()}   %{!S:-o %|.s |
 as %(asm_options) %m.s %A }  }

*cpp:


*cpp_options:
%(cpp_unique_options) %1 %{m*} %{std*&ansi&trigraphs} %{W*&pedantic*} %{w} %{f*} %{g*:%{!g0:%{g*} %{!fno-working-directory:-fworking-directory}}} %{O*} %{undef} %{save-temps*:-fpch-preprocess}

*cpp_debug_options:
%{d*}

*cpp_unique_options:
%{!Q:-quiet} %{nostdinc*} %{C} %{CC} %{v} %{I*&F*} %{P} %I %{MD:-MD %{!o:%b.d}%{o*:%.d%*}} %{MMD:-MMD %{!o:%b.d}%{o*:%.d%*}} %{M} %{MM} %{MF*} %{MG} %{MP} %{MQ*} %{MT*} %{!E:%{!M:%{!MM:%{!MT:%{!MQ:%{MD|MMD:%{o*:-MQ %*}}}}}}} %{remap} %{g3|ggdb3|gstabs3|gcoff3|gxcoff3|gvms3:-dD} %{!iplugindir*:%{fplugin*:%:find-plugindir()}} %{H} %C %{D*&U*&A*} %{i*} %Z %i %{E|M|MM:%W{o*}}

*trad_capable_cpp:
cc1 -E %{traditional|traditional-cpp:-traditional-cpp}

*cc1:
%(cc1_cpu) 

*cc1_options:
%{pg:%{fomit-frame-pointer:%e-pg and -fomit-frame-pointer are incompatible}} %{!iplugindir*:%{fplugin*:%:find-plugindir()}} %1 %{!Q:-quiet} %{!dumpbase:-dumpbase %B} %{d*} %{m*} %{aux-info*} %{fcompare-debug-second:%:compare-debug-auxbase-opt(%b)}  %{!fcompare-debug-second:%{c|S:%{o*:-auxbase-strip %*}%{!o*:-auxbase %b}}}%{!c:%{!S:-auxbase %b}}  %{g*} %{O*} %{W*&pedantic*} %{w} %{std*&ansi&trigraphs} %{v:-version} %{pg:-p} %{p} %{f*} %{undef} %{Qn:-fno-ident} %{Qy:} %{-help:--help} %{-target-help:--target-help} %{-version:--version} %{-help=*:--help=%*} %{!fsyntax-only:%{S:%W{o*}%{!o*:-o %b.s}}} %{fsyntax-only:-o %j} %{-param*} %{coverage:-fprofile-arcs -ftest-coverage}

*cc1plus:


*link_gcc_c_sequence:
%G %L %G

*link_ssp:
%{fstack-protector|fstack-protector-all|fstack-protector-strong|fstack-protector-explicit:-lssp_nonshared -lssp}

*endfile:
crtend.o%s

*link:


*lib:
-lc -lg -lm

*link_gomp:


*libgcc:
-lgcc

*startfile:
%{!shared: 			 %{!symbolic: 			  %{pg:gcrt0.o%s}%{!pg:%{p:mcrt0.o%s}%{!p:crt0.o%s}}}}			crtbegin.o%s

*cross_compile:
1

*version:
6.2.0

*multilib:
. ;

*multilib_defaults:


*multilib_extra:


*multilib_matches:


*multilib_exclusions:


*multilib_options:


*multilib_reuse:


*linker:
collect2

*linker_plugin_file:


*lto_wrapper:


*lto_gcc:


*post_link:


*link_libgcc:
%D

*md_exec_prefix:


*md_startfile_prefix:


*md_startfile_prefix_1:


*startfile_prefix_spec:


*sysroot_spec:
--sysroot=%R

*sysroot_suffix_spec:


*sysroot_hdrs_suffix_spec:


*self_spec:


*cc1_cpu:
%{march=native:%>march=native %:local_cpu_detect(arch)   %{!mtune=*:%>mtune=native %:local_cpu_detect(tune)}} %{mtune=native:%>mtune=native %:local_cpu_detect(tune)}

*link_command:
%{!fsyntax-only:%{!c:%{!M:%{!MM:%{!E:%{!S:    %(linker) %{!fno-use-linker-plugin:%{!fno-lto:     -plugin %(linker_plugin_file)     -plugin-opt=%(lto_wrapper)     -plugin-opt=-fresolution=%u.res     %{!nostdlib:%{!nodefaultlibs:%:pass-through-libs(%(link_gcc_c_sequence))}}     }}%{flto|flto=*:%<fcompare-debug*}     %{flto} %{fno-lto} %{flto=*} %l %{no-pie:} %{pie:-pie} %{fuse-ld=*:-fuse-ld=%*}  %{gz*:%e-gz is not supported in this configuration} %X %{o*} %{e*} %{N} %{n} %{r}    %{s} %{t} %{u*} %{z} %{Z} %{!nostdlib:%{!nostartfiles:%S}}     %{static:} %{L*} %(mfwrap) %(link_libgcc) %{!nostdlib:%{fvtable-verify=std: -lvtv -u_vtable_map_vars_start -u_vtable_map_vars_end}    %{fvtable-verify=preinit: -lvtv -u_vtable_map_vars_start -u_vtable_map_vars_end}} %{!nostdlib:%{!nodefaultlibs:%{%:sanitize(address):}     %{%:sanitize(thread):}     %{%:sanitize(leak):}}} %o      %{fopenacc|fopenmp|%:gt(%{ftree-parallelize-loops=*:%*} 1):	%:include(libgomp.spec)%(link_gomp)}    %{fcilkplus:%:include(libcilkrts.spec)%(link_cilkrts)}    %{fgnu-tm:%:include(libitm.spec)%(link_itm)}    %(mflib)  %{fsplit-stack: --wrap=pthread_create}    %{fprofile-arcs|fprofile-generate*|coverage:-lgcov} %{!nostdlib:%{!nodefaultlibs:%{%:sanitize(address):%{static-libasan:-Bstatic} -lasan %{static-libasan:-Bdynamic} %{static-libasan:%:include(libsanitizer.spec)%(link_libasan)}    %{static:%ecannot specify -static with -fsanitize=address}}    %{%:sanitize(thread):%{static-libtsan:-Bstatic} -ltsan %{static-libtsan:-Bdynamic} %{static-libtsan:%:include(libsanitizer.spec)%(link_libtsan)}    %{static:%ecannot specify -static with -fsanitize=thread}}    %{%:sanitize(undefined):%{static-libubsan:-Bstatic} -lubsan %{static-libubsan:-Bdynamic} %{static-libubsan:%:include(libsanitizer.spec)%(link_libubsan)}}    %{%:sanitize(leak):%{static-liblsan:-Bstatic} -llsan %{static-liblsan:-Bdynamic} %{static-liblsan:%:include(libsanitizer.spec)%(link_liblsan)}}}}     %{!nostdlib:%{!nodefaultlibs:%(link_ssp) %(link_gcc_c_sequence)}}    %{!nostdlib:%{!nostartfiles:%E}} %{T*}
%(post_link) }}}}}}
