import click

def read_file(f):
    with open(f) as r:
        lines = r.readlines()
        return lines

def sum_cn(s):
    a, b = s.split('|')
    a, b = int(a), int(b)
    return a + b

def pair_cn(s):
    a, b = s.split('|')
    a, b = int(a), int(b)
    return max(a, b), min(a, b)

def calc_overlap(bin_s, bin_e, gene_s, gene_e):
    bin_s, bin_e, gene_s, gene_e = int(bin_s), int(bin_e), int(gene_s), int(gene_e)
    return min(bin_e, gene_e) - max(bin_s, gene_s)

def find_bin_to_segment(segments, bin_loc):
    bin_chrm, bin_s, bin_e = bin_loc
    for seg in segments.keys():
        seg_chrm, seg_s, seg_e = seg
        if seg_chrm == bin_chrm:
            # same chrm
            o = calc_overlap(bin_s, bin_e, seg_s, seg_e)
            if o > 0: 
                #print(segments[(seg_chrm, seg_s, seg_e)]) #seg_chrm, seg_s, seg_e, "overlaps", bin_s, bin_e)
                return segments[(seg_chrm, seg_s, seg_e)]

@click.command()
@click.argument('simulated_samples')
@click.argument('simulated_cn')
def main(simulated_samples, simulated_cn):
    print("simulated_samples", simulated_samples)
    print("simulated_cn", simulated_cn)

    ss = read_file(simulated_samples)
    scn = read_file(simulated_cn)
    annotated_simulated_samples = simulated_samples[:-3] + '_cn_annotated_maxmin.bb' 

    loc_to_cid = dict()
    cluster_dict = dict()
    ids = 0
    for line in scn[1:]:
        c, s, e = line.split()[0:3]
        cns = line.split()[3:]
        cns = map(pair_cn, cns) #, pair_cn)
        #cns.sort(key=pair_cn)
        cg = tuple(cns) #(c0, c1) if sum_cn(c0) > sum_cn(c1) else (c1, c0)
        if cg not in cluster_dict.keys():
            cluster_dict[cg] = ids
            ids += 1
        cluster = cluster_dict[cg]
        loc_to_cid[(c,s,e)] = cluster

    for cg in cluster_dict:
        print(cg, cluster_dict[cg])

    with open(annotated_simulated_samples, "w+") as w: 
        w.write("#CHR\tSTART\tEND\tSAMPLE\tRD\t#SNPS\tCOV\tALPHA\tBETA\tBAF\tCLUSTER\n")
        #w.write(ss[0][:-1] + '\tCLUSTER\n')
        for line in ss[1:]:
            c, s, e = line.split()[0:3] #, sample, rd, numsnps, cov, a, b, baf = line.split()
            segment_cluster = find_bin_to_segment(loc_to_cid, (c, s, e))
            sj = '\t'.join(line.split() + [str(segment_cluster)]) + '\n' 
            # c, s, e, sample, rd, numsnps, cov, a, b, baf, str(segment_cluster)]) + '\n'
            w.write(sj)

if __name__ == "__main__":
    main()
