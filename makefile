main:
	mkdir output
	cd source; make

clean:
	rm -rf output
	cd source; make clean

test:
	cd source; make test
	